def queries(collection):
    print("Top 3 highest average temperatures.:")
    for element in collection.find({},{"Country", "AverageTemperature"}).sort("AverageTemperature", -1).limit(3):
        print(element)
    
    print("Top 10 lowest average temperature:")
    for element in collection.find({},{"Country", "AverageTemperature"}).sort("AverageTemperature", 1).limit(3):
        print(element)