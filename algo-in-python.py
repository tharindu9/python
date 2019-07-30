#fibonachi


n0 = 0;
n1 =1;
ans =0;
for i in range(7):
    if(i==0):
        print(n0 , end=" ");

    elif(i==1):
        print(n1 , end=" ");

    else:
        ans = n0+n1;
        n0=n1;
        n1=ans;
        print(ans , end=" ")
