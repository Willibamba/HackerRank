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
            print item

mapReducer = MapReduce()

def mapper(record):
    #Start writing the Map code here
    # Split the records, map SSN as key and (department or employee) and (department name or employee name) as values 
    record = record.strip("\n").split(",")
    if record[0] == "Department":
        mapReducer.emitIntermediate(key=record[1], value=[record[0],record[2]])
    elif record[0] == "Employee":
       mapReducer.emitIntermediate(key=record[2], value=[record[0], record[1]])
           
def reducer(key, list_of_values):
    #Start writing the Reduce code here
    employees = []
    departments = []
    # Iterate list of values and append the values in their respective arrays
    for k, v in list_of_values:
        if k == "Employee":
            employees.append(v)
        else:
            departments.append(v)
    # Iterate departments and employees arrays and join the key, employee name and department as tuple and emit it  
    for department in departments:
        for emp_name in employees:
            mapReducer.emit((key, emp_name, department))
          
                
if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
