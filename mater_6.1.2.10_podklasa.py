class Stack:
    def __init__(self): 
        self.__stackList = [] 

    def push(self, val): 
        self.__stackList.append(val) 

    def pop(self): 
        val = self.__stackList[-1] 
        del self.__stackList[-1] 
        return val 

class AddingStack(Stack): 
    def __init__(self):         #konstruktor nadklasy wywołany jawnie
        Stack.__init__(self) 
        self.__sum = 0          #prywatna własność suma

    def push(self, val):        #nadpisanie metody push, nowa funkcjonalnosc
        self.__sum += val 
        Stack.push(self, val)   #obiekt docelowy metody

    def pop(self): 
        val = Stack.pop(self) 
        self.__sum -= val 
        return val

    def getSum(self): 
        return self.__sum


stackObject = AddingStack() 

for i in range(5): 
    stackObject.push(i) 
print(stackObject.getSum()) 

for i in range(5): 
    print(stackObject.pop())
