from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
CORS(app) 
# Connect to MongoDB
mongodb_uri=os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)
db = client['emptycup']  
collection = db['assignment']  

@app.route('/', methods=['GET'])
def get_data():
    data_from_mongo = list(collection.find({}, {'_id': 0}))
    return jsonify(data=data_from_mongo)

if __name__ == '__main__':
    app.run()
