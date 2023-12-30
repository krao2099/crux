from flask import Flask, request, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from models.crag import Crag
from db import setPass
from psycopg2.errors import UniqueViolation
from crux_utils import is_admin
import os

app = Flask(__name__)


setPass()

def set_cookie_response(response, username):
    response = make_response(response)
    user_id_username_union = str(User.login_success(username)) + ":" + username
    response.set_cookie('user_id', user_id_username_union, httponly=True, samesite='lax')
    return response

@app.route('/user', methods=['POST'])
async def create_user():
    user_cookie = request.cookies.get('user_id')
    if user_cookie:
        return jsonify({'success': 'logged_in_user'}), 200
    data = request.json
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing Data !'}), 400
    new_user = User(
        None,
        None,
        data['username'],
        data['email'],
        generate_password_hash(data['password'])
    )
    try:
        new_user.create_user()
    except Exception as e:
        if type(e) is UniqueViolation:
            return jsonify({'error': 'Duplicate Username !'}), 400
        print(str(e))
        return jsonify({ 'error' : 'Unknown server error'}), 500
    response = set_cookie_response(jsonify({'success': 'User created !'}), data['username'])
    return response, 200

@app.route('/login', methods=['POST'])
async def login():
    data = request.json
    user_cookie = request.cookies.get('user_id')
    if user_cookie:
        #TODO validation
        return jsonify({'success': 'logged_in'}), 200
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing Data !'}), 400
    h_pass = User.retrieve_hash_password(data['username'])
    if h_pass == "lockout" or h_pass == "fail_login":
        return jsonify({'error': h_pass}), 200
    if check_password_hash(h_pass, data['password']):
        response = set_cookie_response(jsonify({'success': 'logged_in'}), data['username'])
        return response, 200
    return jsonify({'error': 'fail_login'}), 200

@app.route('/user_details', methods=['GET'])
async def user_details():
    response = {
        'logged_in': False,
        'admin': False,
        'username': ''
    }
    user_cookie = request.cookies.get('user_id')
    if user_cookie == 'null':
        return jsonify(response), 200
    user_cookie = user_cookie.split(":")
    #TODO add valid auth that return id and username
    response['logged_in'] = True
    response['admin'] = is_admin(user_cookie[0])
    response['username'] = user_cookie[1]
    return jsonify(response), 200

    

@app.route('/logout', methods=['POST'])
async def logout():
    user_cookie = request.cookies.get('user_id')
    if not user_cookie:
        return jsonify({'error': 'No User Data'}), 200
    response = make_response(jsonify({'success': 'logged_out'}))
    response.delete_cookie('user_id')
    return response, 200

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