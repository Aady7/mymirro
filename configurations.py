
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://aadiItis:ainyboo@mymirro.fs9yt.mongodb.net/?retryWrites=true&w=majority&appName=MyMirro"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db= client["myMirro"]

user_collection = db["users"]
product_collection = db["products"]
recommendation_collection = db["recommendations"]

