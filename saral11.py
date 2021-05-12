my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max=0
empty=[]
for i in my_dict:
    count=0
    for j in my_dict:
        if my_dict[i]>my_dict[j]:
            max=my_dict[i]
            count+=1
        if count==3:
            empty.append(max)
            break
print(empty)
# three highest value,[58,56,100]


