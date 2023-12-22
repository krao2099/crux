import pytest

import sys
sys.path.append('../Server/models')
sys.path.append('../Server')

from user import User
import db


def test_create_user():
    test_user = User(None, None, "testUser", "testemail@email.com", "testPassword")

    test_user.create_user()

    query = "SELECT * FROM Users WHERE username = 'testUser'"

    result = db.retrieve(query, None)

    assert "testUser" in result




    

