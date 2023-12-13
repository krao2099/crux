from flask import Flask, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)



@app.route('/test', methods=['GET'])
async def test():
    return jsonify({'message': 'Server is working!'}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)