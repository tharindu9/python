class stack: # create stack class
    def __init__(self):
        self.items=[]


    def isEmpty(self):#empty stack
        return self.items==[]

    def pop(self):#return the top index vale
        return self.items.pop()

    def push(self,item):#inserting to stasck
        return self.items.append(item)

    def peek(self):#show only the top index value
        return self.items[len(self.items)-1]

    def size(self):#size of stack
        return len(self.items)

s=stack() #s is a object of stack
s1=stack() # object of stack
n=int(raw_input("enter num\n")) # take the number what want to convert
while n>0:
    if n%2==0: #check weather  n modul by 2
        s.push(0) 
    else:
        s.push(1)
    n=n//2


while not s.isEmpty(): #take out the s stack
      s1.push(s.pop()) # fill the s1 pasing values of s

    
print(str(s1.items)) #items of s1  display as qithin a []
print ("Binary value ")
for x in s1.items:
    print(x), #items of s1 
    
        
        
