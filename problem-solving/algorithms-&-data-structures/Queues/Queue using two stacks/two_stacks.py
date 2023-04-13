# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:
    def __init__(self):
        self._data = []    
        
    def enqueue(self, value):
        self._data.append(value)
        
    def deque(self):
        self._data.pop(0)
    
    def peek_first(self):
        return self._data[0]
    
     
if __name__ == '__main__':
    stack = Stack()
    
    q = int(input())
    for _ in range(q):
        stdin = str(input()).split(" ")
        query = int(stdin[0])
        
        if query == 1:
            stack.enqueue(int(stdin[1]))       
        
        elif query == 2:
           stack.deque()
        
        else:
            print(stack.peek_first())