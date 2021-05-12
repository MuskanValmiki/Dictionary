d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in d1:
    for j in d2:
        if i==j:
            dic[i]=d1[i]+d2[j]
            break
    else:
        dic[i]=d1[i]
        dic[j]=d2[j]
print(dic)
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# 2nd way
for i in d2:
    if i in d1:
        d2[i]+=d1[i]
temp={**d1,**d2}
print(temp)

