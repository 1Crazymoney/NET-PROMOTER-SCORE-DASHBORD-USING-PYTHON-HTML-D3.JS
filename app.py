from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# Load data from JSON file
with open('nps_data.json', 'r') as f:
    data = json.load(f)

@app.route('/nps_data')
def get_nps_data():
    return jsonify(data)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
