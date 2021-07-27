i=1
while i<=3:
    j=1
    while j<=5:
        if (i==2 and(j==1 or j==5)):
            print(" ",end=" ")
        elif(i==3 and(j==1 or j==2 or j==4 or j==5)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        j=j+1
    print()
    i=i+1    