d=[{"a":"S001"},{"b": "S002"},{"c": "S001"},{"d": "S005"},{"e":"S005"},{"f":"S009"},{"g":"S007"}]
d1=[]
test=[]
for i in range(0,len(d)):
    for key,value in d[i].items():
        if d[i][key]!=d1:
            d1=d[i][key]
        if d1 not in test:
            test.append(d1)
print(test)
# unique value['S001', 'S002', 'S005', 'S009', 'S007']



