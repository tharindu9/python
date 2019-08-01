class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


for i in range(1,9):
    print("*", end=" ")
    if(i==3):
        print("*","*")
        for j in range(1,5):
            print(" " , " ","*")

print()

for x in range(1,6):

    if(x==1):
        print()
        print(color.RED +"  *","   *" + color.END)
    if(x==2):
        print(color.RED +"*   *","   *" +color.END)
    if(x==3):
        print(color.RED  +"*","  "*3 , "*" +color.END)
    if(x==4):
        print(color.RED +"  *","  ","*  " +color.END)
    if(x==5):
        print(color.RED +"   ","*" ,"  " +color.END)

print()

for k in range(1,6):
    if(k==1):
        for l in range(1,4):
            if(i!=3):
                print("*"," "*3,"*")
            else:
                print("*",end="")
    elif(k==2 or k==5):
        print(" ",end=" ")

    else:
        print("*", end=" ")


#sys.stdout.write('\x1b[1;34m' + "tharindu rukshan" + '\x1b[0m' )


