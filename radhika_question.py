i=1
while i<=4:
    j=1
    while j<=4:
        if (i==1 and(j==2 or j==3)) or (i==4 and(j==2 or j==3)):
            print(" ",end=" ")
        else:
            print("*",end=" ")
        j=j+1
    print()
    i=i+1    