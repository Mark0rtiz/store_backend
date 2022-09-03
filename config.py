import pymongo
import certifi

con_str = "mongodb+srv://mortiz009:testPassword123@cluster0.cx2ridb.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("OnlineStore")