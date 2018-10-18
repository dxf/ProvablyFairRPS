from pymongo import MongoClient
print('Rock Paper Scissors Result Validator')
print()
rid = input("Insert result ID: ")
client = MongoClient('YOUR_MONGO_ADDRESS')
db = client.rpsvalidator
collection = db.results
x = collection.find_one({"resultid":rid})
try:
    print('Computer:')
    print(x["computer"])
    print('Player:')
    print(x["player"])
except:
    print('Invalid result ID!')

