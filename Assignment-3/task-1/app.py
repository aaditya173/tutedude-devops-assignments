from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Home page route
@app.route('/')
def home():

    return "Welcome to the Home Page!."

# Api route for request the data from the backend file
@app.route('/api')
def get_data():
    # Get absolute path to data.json
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    
    # Read data from file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Return the data of the backend file to the api route
    return jsonify(data)

if __name__ == '__main__':
    app.run()
