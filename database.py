from pymongo import MongoClient

# 1. Establish a connection to the MongoDB server
client = MongoClient("mongodb://db:27017/")

# 2. Access the specific database and collection
db = client["school_database"]

# 3. Define collections for pupils, teachers, and classes
pupils_collection = db["pupils"]
teachers_collection = db["teachers"]
lessons_collection = db["lessons"]

print("Successfully connected to MongoDB!")