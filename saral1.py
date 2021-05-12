# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# empty={}
# for i in dic1:
#     for j in dic2:
#         if i==j:
#             empty[i]=dic1[i]+dic2[j]
# print(empty)
# if same key to sum{2:60}
dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d={}
for i in dic2:
    if i in dic1:
        dic2[i]+=dic1[i]
d={**dic1,**dic2,**dic3}
print(d)
# {1: 10, 2: 60, 3: 30, 5: 50, 6: 60}