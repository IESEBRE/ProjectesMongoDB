import pprint
import json
from bson import json_util
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['prova']  # Database name
#collection = db['restaurants']  # Collection name
collection = db.restaurants  # Collection name

# Sample route to retrieve restaurants
@app.route('/restaurants')
def get_restaurants():
    # Query all restaurants from the collection
    restaurants = collection.find()

    # Convert restaurant documents to a list of dictionaries
    restaurant_list = [{'name': restaurant['name'], 'cuisine': restaurant['cuisine']} for restaurant in restaurants]

    return jsonify(restaurant_list)

@app.route('/un_restaurant')
def get_one_restaurant():
    # Query the first restaurants from the collection
    restaurant = collection.find_one({"name": "4 Vientos"})
    pprint.pprint(restaurant)
    # Convert restaurant documents to a list of dictionaries
    #restaurant_list = [{'name': restaurant['name'], 'cuisine': restaurant['cuisine']} for restaurant in restaurants]

    #https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
    #return jsonify(restaurant) #TypeError:  is not JSON serializable
    return parse_json(restaurant)

@app.route('/add_restaurant')
def add_restaurant():
    # Query all restaurants from the collection
    restaurant={'name': '4 Vientos x 5', 'cuisine': 'De interiorrrrr'}
    collection.insert_one(restaurant)

    # Convert restaurant documents to a list of dictionaries
    restaurant_list = collection.find_one({'name': '4 Vientos', 'cuisine': 'De interior'},{'name':1})

    #return 'insertat'
    return jsonify(restaurant)




def parse_json(data):
    return json.loads(json_util.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)