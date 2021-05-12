item_list=[{'item': 'item1','amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750},{'item':'item2','amount':100}]
d1={}
sum=0
sum1=0
for i in item_list:
    if "item1" in i["item"]:
        sum=sum+i["amount"]
        d1["item1"]=sum
    else:
        sum1=sum1+i["amount"]
        d1["item2"]=sum1
print(d1)

