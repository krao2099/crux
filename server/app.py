from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from models.crag import Crag
from db import setPass
from psycopg2.errors import UniqueViolation
import os

app = Flask(__name__)

#TODO change the env var
app.config['SECRET_KEY'] = 'feBOBFEO'

setPass()


@app.route('/user', methods=['POST'])
async def create_user():
    data = request.json
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'Error': 'Missing Data !'}), 400
    new_user = User(
        None,
        None,
        data['username'],
        data['email'],
        generate_password_hash(data['hash_password'])
    )
    try:
        new_user.create_user()
    except Exception as e:
        if type(e) is UniqueViolation:
            return jsonify({'Error': 'Duplicate Username !'}), 400
        return jsonify({ 'Error' : str(e)}), 500
    session['user_id'] = new_user.id
    return jsonify({'Success': 'User created !'}), 200

@app.route('/login', methods=['POST'])
async def login():
    if session['user_id']:
        return jsonify({'message': 'logged_in'}), 200
    data = request.json
    if 'username' not in data or 'password' not in data:
        return jsonify({'Error': 'Missing Data !'}), 400
    h_pass = User.retrieve_hash_password(data['username'])
    if h_pass == "lockout" or h_pass == "fail_login":
        return jsonify({'Error': h_pass}), 200
    if check_password_hash(h_pass, data['password']):
        session['user_id'] = User.login_success(data['username'])
        return jsonify({'Success': 'logged_in'}), 200
    return jsonify({'Error': 'fail_login'}), 200

@app.route('/logout', methods=['POST'])
async def logout():
    if not session['user_id']:
        return jsonify({'Error': 'No User Data'}), 200
    session.pop('user_id', default=None)
    return jsonify({'Success': 'logged_out'}), 200

@app.route('/crag', methods=['POST'])
def create_crag():
    data = request.json
    new_crag = Crag(
        None,
        None,
        data.get('name', None),
        data.get('state', None),
        data.get('coordinates', None),
        data.get('description', None),
        data.get('image', None),
        None,
        data.get('user', None)
    )
    new_crag.create_crag()
    return jsonify({'message': 'Crag created !'}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working!'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)