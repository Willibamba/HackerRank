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
        self.result[value[0]][value[1]] = value[2]


    def execute(self, matrix1, matrix2, mapper, reducer):
        n = len(matrix1)
        m = len(matrix2[0])
        for i in xrange(0, n):
            self.result.append([0] * m)

        mapper(matrix1, matrix2)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for i in xrange(0, n):
            row = ""
            for j in xrange(0, m):
                row += str(self.result[i][j]) + " "
            print(row)

mapReducer = None

def mapper(matrix1, matrix2):
    # Start writing the Map code here
    # Iterate through the length of matrix and matrix2[0] for indices i and j respectively
    for i in xrange(len(matrix1)):
        for j in xrange(len(matrix2[0])):
            # Iterate through matrix1[0] for indices k
            for k in range(len(matrix1[0])):
                # Emit indices i and j as keys and the values of matrices wih their respective indices as values
                mapReducer.emitIntermediate((i,j), (matrix1[i][k], matrix2[k][j]))

def reducer(key, list_of_values):
    # Start writing the Reduce code here
    # Emit key values and compute the list_of_values as tuples
    mapReducer.emit((key[0], key[1], sum(k * v for k, v in list_of_values)))

if __name__ == '__main__':
    testcases = int(raw_input())
    for _ in xrange(testcases):
        mapReducer = MapReduce()
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        matrix1 = []
        matrix2 = []
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix1.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix1[i].append(int(row_elems[j]))
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        
        for i in range(row):
            read_row = sys.stdin.readline().strip()
            matrix2.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix2[i].append(int(row_elems[j]))
        
        mapReducer.execute(matrix1, matrix2, mapper, reducer)
