import pytest

import sys
sys.path.append('../Server/models')
sys.path.append('../Server')

from user import User, retrieve_hash_password, login_success
import db
from datetime import datetime
import pytz

import psycopg2

test_user = None
@pytest.fixture
def setup_data():
    query = "DELETE FROM Users"
    db.execute(query, None)
    global test_user 
    test_user = User(None, None, "testUser", "testemail@email.com", "testPassword")
    test_user.create_user()
    
def select_test_user():
    query = "SELECT * FROM Users WHERE username = 'testUser';"

    return db.retrieve(query, None)
def test_create_user(setup_data):
    result = select_test_user()

    assert len(result) == 1
    assert "testUser" in result[0]

    second_user = User(None, None, "testUser", "testemail@email.com", "testPassword")

    with pytest.raises(psycopg2.errors.UniqueViolation) as excinfo:  
        second_user.create_user()

    assert str(excinfo.value).__contains__('duplicate key value violates unique constraint "users_username_key"')

def test_retrieve_hash_password(setup_data):

    result = retrieve_hash_password("fakeUser")

    assert result == "fail_login"
    result = retrieve_hash_password("testUser")
    
    assert result == "testPassword"

    for i in range(10):
        retrieve_hash_password("testUser")
    
    result = retrieve_hash_password("testUser")

    assert result == "lockout"

def test_login_success(setup_data):
    result = login_success("testUser")

    assert result is not None

    result = select_test_user()

    print(result)

    assert result[0][6] == 0

    now = datetime.now()
    now = now.astimezone(pytz.utc)

    ttl = result[0][7]
    ttl = ttl.replace(tzinfo=pytz.timezone('UTC'))
    assert  now > ttl