class stack:
    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return self.items==[]

    def pop(self):
        return self.items.pop()

    def push(self,item):
        return self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=stack()
s1=stack()
n=int(raw_input("enter num\n"))
while n>0:
    if n%2==0:
        s.push(0)
    else:
        s.push(1)
    n=n//2


while not s.isEmpty():
      s1.push(s.pop())

    
print(str(s1.items))
print ("Binary value ")
for x in s1.items:
    print(x),
    
        
        
