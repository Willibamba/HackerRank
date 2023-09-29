import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
   	self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print "{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}"

mapReducer = MapReduce()

def mapper(record):
    #Start writing the Map code here
    # strip new-line from record and Split the names by space 
    record = record.strip("\n").split(" ")
    # Map (record[0] as key, record[1] as value) and (record[1] as key, record[0] as value)
    mapReducer.emitIntermediate(record[0], record[1])
    mapReducer.emitIntermediate(record[1], record[0])

def reducer(key, list_of_values):
    #Start writing the Reduce code here
    # Emit key as Person name and length of list_of_values as number of friends
    mapReducer.emit((key, len(list_of_values)))
    
if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)