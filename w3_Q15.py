d= {'x':500, 'y':5874, 'z': 560}
key_max = max(d.keys(), key=(lambda k: d[k]))
key_min = min(d.keys(), key=(lambda k: d[k]))
print('Maximum Value: ',d[key_max])
print('Minimum Value: ',d[key_min])

d={"a":100,"b":5009,"c":1500}
min=d["a"]
for i in d:
    if d[i]<min:
        min=d[i]
print("minimum=",min)
