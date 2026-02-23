from flask import Flask, render_template, request   
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

client = pymongo.MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]

app = Flask(__name__)

@app.route('/')
def registraion():

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = dict(request.form) 
        collection.insert_one(data)
        return "Data submitted successfully!"
    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
