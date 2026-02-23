from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

# MongoDB Connection
client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    todo_item = dict(request.form)

    collection.insert_one(todo_item)

    return jsonify({"message": "To-Do item saved successfully!"})

if __name__ == "__main__":
    app.run(port="9000", debug=True)
