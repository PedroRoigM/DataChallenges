from pymongo import MongoClient
from pandas import read_excel

def initApp(collection_names: str, uri='mongodb://localhost:27017/', db_name='GLobalLandTemperature'):
    data = read_excel("Data/GlobalLandTemperaturesByCity_Cleaned.xlsx", nrows=10000)
    
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_names]
    
    data.apply(lambda row: insertData(row, collection), axis=1)
    return collection


def insertData(row, collection):
    collection.create_index("dt")
    document = row.to_dict()
    collection.insert_one(document)
    