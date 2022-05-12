
import pymongo

def connect_mongo_db(MONGO_URI):
    mongoclient = pymongo.MongoClient(MONGO_URI)
    try:
        mongoclient.server_info()
        return mongoclient
    except:
        print("ERROR! TRY CHECK STATUS MONGO")

def create_mongo_db(mongoclient):
    #DROP DATABASE IF IT EXIST
    try:
        mongoclient.drop_database("mydatabase")    
    except:
        pass
    mongo_mydb = mongoclient["mydatabase"]
    return mongo_mydb
    