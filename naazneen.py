n=int(input("enter a number"))
i=0
while n>0:
    N=n%10
    i=i*10+N
    n=n//10
print(i)