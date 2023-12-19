from flask import Flask, request, jsonify
from dotenv import load_dotenv
from models.user import user
import os

app = Flask(__name__)



@app.route('/user', methods=['POST'])
async def create_user():
    data = request.json
    new_user = user(None, data.name, data.grade, data.rating, data.style, data.height, data.safety, data.image, data.FA, data.setter, data.wall, data.numBolts, data.pads, data.coordinates, data.danger, data.description)
    new_user.create_user()
    return jsonify({'message': 'User created !'}), 200

@app.route('/test', methods=['GET'])
async def test():
    return jsonify({'message': 'Server is working!'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)