import sys


for i in range(1,9):
    print("#", end=" ")
    if(i==3):
        print("#","#")
        for j in range(1,5):
            print(" " , " ","#")

print('\n')
for k in range(1,6):
    if(k==1):
        for l in range(1,4):
            if(i!=3):
                print("#")
            else:
                print("#",end="")


    else:
        print("#" , end=" ")

print("\n")

for k in range(1, 6):
    if (k == 1):
        for l in range(1, 4):
            if (i != 3):
                print("#")
            else:
                print("#", end="")


    else:
        print("#", end=" ")

#sys.stdout.write('\x1b[1;34m' + "tharindu rukshan" + '\x1b[0m' )


