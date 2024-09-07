from pymongo import MongoClient

# Setup MongoDB here
 
CONNECTION_STRING = "mongodb+srv://2nakshtra:eBhpivQBYpWz5jDE@naksh.g4fw4e0.mongodb.net/"
 
client = MongoClient(CONNECTION_STRING)
 
# Create the database 

db = client['webhook_db']

# Define the Collection
events_collection = db['events']