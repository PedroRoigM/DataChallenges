
from queries import queries
from model import  initApp 

def __main__():
    print("Initializing data")
    
    collection = initApp("DataCollection")
    print("Data initialized")
    
    
    queries(collection)

if __name__ == '__main__':
    __main__()