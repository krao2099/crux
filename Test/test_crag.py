import psycopg2
import pytest

import sys
sys.path.append('../Server/models')
sys.path.append('../Server')

from user import User
from crag import Crag, publish_crag
import db

test_crag = None
test_user = None
admin_id = None

@pytest.fixture
def setup_data():

    query = "DELETE FROM Crags"
    db.execute(query, None)


    query = "DELETE FROM Users WHERE admin_flag = FALSE"
    db.execute(query, None)

    global test_crag
    global test_user
    global admin_id

    test_user = User(None, None, "testUser", "testemail@email.com", "testPassword")
    test_user.create_user()

    test_crag = Crag(None, None, "testCrag", "North Carolina", [35.7851, 78.6813], "A great crag", "image", 5, test_user.id)
    test_crag.create_crag()

    query = "SELECT id from Users WHERE username = 'admin'"
    admin_id = db.retrieve(query, None)[0][0]


def select_test_crag():
    query = "SELECT * FROM Crags WHERE name = 'testCrag'"
    return db.retrieve(query, None)

def test_create_crag(setup_data):
    result = select_test_crag()

    assert len(result) == 1
    assert "testCrag" in result[0]

def test_publish_crag(setup_data):
    result = select_test_crag()

    assert result[0][9] == False

    with pytest.raises(PermissionError) as excinfo:  
        publish_crag(test_user.id, test_crag.id)
    assert str(excinfo.value).__contains__('admin privelages required for publishing')

    publish_crag(admin_id, test_crag.id)
    result = select_test_crag()
    assert result[0][9] == True
