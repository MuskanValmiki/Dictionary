dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sorted_value=sorted(dic.values())
# empty_dic={}
# for i in sorted_value:
#     for j in dic.keys():
#         if dic[j]==i:
#             empty_dic[j]=dic[j]
#             break
# print(empty_dic)
# assending {'param': 20, 'anjili': 30, 'bijender': 45, 'roshini': 50, 'deepak': 60}

key=[]
value=[]
for i in dic:
    key.append(i)
    value.append(dic[i])
for j in range(0,len(value)):
    for k in range(0,len(value)):
        if value[j]>value[k]:
            value[j],value[k]=value[k],value[j]
            key[j],key[k]=key[k],key[j]
desending={}
for l in range(0,len(key)):
    desending[key[l]]=value[l]
print(desending)
# {'deepak': 60, 'roshini': 50, 'bijender': 45, 'anjili': 30, 'param': 20}

key=[]
value=[]
for i in dic:
    key.append(i)
    value.append(dic[i])
for j in range(0,len(value)):
    for k in range(0,len(value)):
        if value[j]<value[k]:
            value[j],value[k]=value[k],value[j]
            key[j],key[k]=key[k],key[j]
assending={}
for l in range(0,len(key)):
    assending[key[l]]=value[l]
print(assending)
# {'param': 20, 'anjili': 30, 'bijender': 45, 'roshini': 50, 'deepak': 60}
