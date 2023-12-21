from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from models.crag import Crag
from db import setPass
import os

app = Flask(__name__)

#TODO change the env var
app.config['SECRET_KEY'] = 'feBOBFEO'

setPass()


@app.route('/user', methods=['POST'])
async def create_user():
    data = request.json
    if 'username' not in data or 'email' not in data or 'hash_password' not in data:
        return jsonify({'message': 'Missing Data !'}), 400
    new_user = User(
        None,
        None,
        data['username'],
        data['email'],
        generate_password_hash(data['hash_password'])
    )
    new_user.create_user()
    return jsonify({'message': 'User created !'}), 200

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