import pytest

import sys
sys.path.append('../Server/models')
sys.path.append('../Server')

from user import User
import db

import psycopg2

@pytest.fixture
def setup_data():
    query = "DELETE FROM Users"
    db.execute(query, None)

def test_create_user(setup_data):
    test_user = User(None, None, "testUser", "testemail@email.com", "testPassword")

    test_user.create_user()

    query = "SELECT * FROM Users WHERE username = 'testUser';"

    result = db.retrieve(query, None)

    assert len(result) == 1
    assert "testUser" in result[0]

    second_user = User(None, None, "testUser", "testemail@email.com", "testPassword")

    with pytest.raises(psycopg2.errors.UniqueViolation) as excinfo:  
        second_user.create_user()

    assert str(excinfo.value).__contains__('duplicate key value violates unique constraint "users_username_key"')




    

