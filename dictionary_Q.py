l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]
def nested_dictionary(l1, l2, l3):
	     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
	     return result
print(nested_dictionary(l1, l2, l3))

dict1={}
dict2={}
i=0
while i<len(l2):
	dict2[l2[i]]=l3[i]
	i+=1
print(dict2)
index=0
while index<len(l1):
	dict1[l1[index]]=dict2
	index+=1
print(dict1)

d={"science":[88,89,62,95],"language":[77,78,84,80]}
key =[]
value=[]
for i in d:
	key.append(i)
	value.append(d[i])
print(key)
print(value)

index=0
dict={}
while index<len(value):
	j=0
	while j<len(value[index]):
		j+=1
	dict[key[index]]=value[index][j]
	index+=1
print(dict)
