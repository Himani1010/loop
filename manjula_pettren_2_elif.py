i=1
while i<=4:
    j=1
    while j<=7:
        if (i==1 and(j==1 or j==2 or j==3 or j==5 or j==6 or j==7)):
            print(" ",end=" ")
        elif(i==2 and(j==1 or j==2 or j==6 or j==7)):
            print(" ",end=" ")
        elif(i==3 and(j==1 or j==7)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        j=j+1
    print()
    i=i+1    