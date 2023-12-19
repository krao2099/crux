from flask import Flask, request, jsonify
from models.user import user
import os

app = Flask(__name__)



@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = user(None, None, data.username, data.email, data.hash_password, None, None, None)
    new_user.create_user()
    return jsonify({'message': 'User created !'}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working!'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)