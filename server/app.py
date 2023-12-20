from flask import Flask, request, jsonify
from models.user import User
from models.crag import Crag
from db import setPass
import os

app = Flask(__name__)

setPass()

@app.route('/user', methods=['POST'])
async def create_user():
    data = request.json
    new_user = User(
        None,
        None,
        data.get('username', None),
        data.get('email', None),
        data.get('hash_password', None)
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