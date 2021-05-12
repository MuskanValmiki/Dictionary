# dissending value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for x in d:
    for y in d:
        if d[x]>d[y]:
            m=d[x]
            d[x]=d[y]
            d[y]=m
print(d)
# o/p={1: 4, 3: 3, 4: 2, 2: 1, 0: 0}


# assending value
d={1:2,3:4,4:3,2:1,0:0}
for i in d:
    for j in d:
        if d[i]<d[j]:
            n=d[i]
            d[i]=d[j]
            d[j]=n
print(d)
# o/p={1: 0, 3: 1, 4: 2, 2: 3, 0: 4}
