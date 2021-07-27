num=int(input("Enter a number:"))
a=num
sum=0
while a>0:
    j=1
    f=1
    r=a%10
    while j<=r:
        f=f*j
        j=j+1
    sum=sum+f
    a=a//10
if sum==num:
    print("The number is a strong number")
else:
    print("No!")
