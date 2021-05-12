d={"a":1,"b":2,"c":3,"d":4}
e=[]
f=[]
for i in d:
    e.append(d[i])
    f.append(i)
print(e)
print(f)
j=-1
m={}
while j>=(-len(e)):
    rev=e[j]
    rev1=f[j]
    m[rev1]=rev
    j-=1
print(m)
#it is working because key already assending

for key in sorted(d):
    print(key,d[key])




