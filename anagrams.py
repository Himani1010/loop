a="chin"
b="inch"
c=""
i=0
while i<len(a):
    if a[i]in b:
        c=c+a[i]
    i+=1
if len(a)==len(c):
    print("true")
else:
    print("false") 