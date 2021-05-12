str='w3resource'
dic={}
for i in range(0,len(str)):
    count=1
    if str[i] in dic:
        count+=1
    dic[str[i]]=count
print(dic)
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
#creat a dic with string