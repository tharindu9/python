
for i in range(1,9):
    print("@", end=" ")
    if(i==3):
        print("@","@")
        for j in range(1,5):
            print(" " , " ","@")

print()

for x in range(1,6):

    if(x==1):
        print()
        print("  *","   *")
    if(x==2):
        print("*   *","   *")
    if(x==3):
        print("*","  "*3 , "*")
    if(x==4):
        print("  *","  ","*  ")
    if(x==5):
        print("   ","*" ,"  ")

for k in range(1,6):
    if(k==1):
        for l in range(1,4):
            if(i!=3):
                print("#"," "*3,"#")
            else:
                print("#",end="")


    else:
        print("#" , end=" ")


