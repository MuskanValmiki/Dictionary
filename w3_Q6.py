def square(num):
    d={}
    i=1
    while i<=num:
        d[i]=i*i
        i+=1
    print(d)
num=int(input("enter any number="))
square(num)

d={}
n=int(input("enter any number="))
for i in range(1,n+1):
    d[i]=i*i
print(d)