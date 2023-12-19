from flask import Flask, request, jsonify
from models.user import user
from models.crag import crag
import os

app = Flask(__name__)



@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = user(
        username=data.get('username', None),
        email=data.get('email', None),
        hash_password=data.get('hash_password', None))
    new_user.create_user()
    return jsonify({'message': 'User created !'}), 200

@app.route('/crag', methods=['POST'])
def create_crag():
    data = request.json
    new_crag = crag(
        name=data.get('name', None),
        state=data.get('state', None),
        coordinates=data.get('coordinates', None),
        description=data.get('description', None),
        image=data.get('image', None),
        user=data.get('user', None),
    )
    new_crag.create_crag()
    return jsonify({'message': 'User created !'}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working!'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)