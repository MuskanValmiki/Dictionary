my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
max=0
empty=[]
for i in my_dict:
    count=0
    for j in my_dict:
        if my_dict[i]>my_dict[j]:
            max=my_dict[i]
            key=i
            count+=1
        if count==3:
            empty.append(key)
            break
print("three highest value in key =",empty)
# three highest value in key = ['b', 'c', 'e']