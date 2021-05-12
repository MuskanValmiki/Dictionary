d={"a":1,"b":3,"a":5,"d":6,"b":8}
d1={}
for key ,value in d.items():
    if key not in d1.keys():
        d1[key]=value
print(d1)
