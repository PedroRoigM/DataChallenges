import pandas as pd;
from pymongo import MongoClient;

def initApp(collection_names: str, uri='mongodb://localhost:27017/', db_name='GLobalLandTemperature'):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_names]
    return collection


def insertData(row, collection):
    collection.create_index("dt")
    document = row.to_dict()
    collection.insert_one(document)
    

def __main__():
    print("Initializing data")

    data = pd.read_excel("GlobalLandTemperaturesByCity_Cleaned.xlsx")
    collection = initApp("DataCollection")
    data.apply(lambda row: insertData(row, collection), axis=1)

if __name__ == '__main__':
    __main__()