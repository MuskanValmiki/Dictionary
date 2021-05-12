list=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}] 
dic={}
list1=[]
for i in range(0,len(list)):
    for value in list[i]:
        dic=(list[i][value])
    if dic not in list1:
        list1.append(dic)
print(list1)
# 2', '7', '9', '5', '1'] 
