user=input("enter any word=")
i=0
a=[]
b=[]
while i<len(user):
    j=0
    sum=0
    while j<len(user[i]):
        sum+=ord(user[i][j])
        j+=1
        a.append(sum)
        b.append(user[i])
    k=0
    while k<len(a):
        if a[i]<a[k]:
            a[i],a[k]=a[k],a[i]
            b[i],b[k]=b[k],b[i]
        k+=1
    i+=1
print(b)
print(a)