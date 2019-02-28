#!/usr/bin/env python3
from flask import Flask, jsonify

message = 'Hello, World'
app = Flask(__name__)

@app.route('/api/v1.0/message', methods=['GET'])
def get_message():
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)

