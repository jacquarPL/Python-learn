class Stack:                # definiowanie klasy Stosu 
    def __init__(self):     # definiowanie funkcji konstruktora
        print("Czesc!")

stackObject = Stack()       # tworzenie instancji obiektu


class Stack2: 
    def __init__(self): 
        self.stackList = [] #wlasciwosc

stackObject = Stack2() 
print(len(stackObject.stackList))   #dostep do wlasciwosci


class Stack3: 
    def __init__(self): 
        self.__stackList = []   #wlasciwosc prywatna, dostep tylko z klasy

stackObject = Stack() 
#print(len(stackObject.__stackList)) #BŁĄD - właściwość prywatna

class Stack4: 
    def __init__(self): 
        self.__stackList = [] 

    def push(self, val): 
        self.__stackList.append(val) 

    def pop(self): 
        val = self.__stackList[-1] 
        del self.__stackList[-1] 
        return val


stackObject = Stack4() 

stackObject.push(3) 
stackObject.push(2) 
stackObject.push(1) 

print(stackObject.pop()) 
print(stackObject.pop()) 
print(stackObject.pop())

stackObject1 = Stack4()     #kolejny obiekt klasy Stack4
stackObject2 = Stack4() 

stackObject1.push(3) 
stackObject2.push(stackObject1.pop()) 

print(stackObject2.pop())
