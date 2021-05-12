# num=int(input("enter any number="))
# i=1
# list1=[]
# list2=[]
# while i<=num:
#     name=input("enter any name=")
#     marks=int(input("enter any marks="))
#     list1.append(name)
#     list2.append(marks)
#     i+=1
# j=0
# dic={}
# while j<len(list1):
#     dic[list1[j]]=list2[j]
#     j+=1
# print(dic)

# list1=[]
# list2=[]
# for i in range(0,10):
#     name=input("enter any name=")
#     marks=int(input("enter any marks="))
#     list1.append(name)
#     list2.append(marks)
# dic={}
# for j in range(0,len(list1)):
#     dic[list1[j]]=list2[j]
# print(dic)

dic={}
for i in range(0,10):
    name=input("enter any name=")
    marks=int(input("enter any marks="))
    dic[name]=marks
print(dic)

# {'aditya': 98, 'kajal': 78, 'muskan': 80, 'kashish': 89, 'sajal': 67, 'sanu': 70, 'kittu': 63, 'sneha': 68, 'sunny': 72, 'kartik': 90}
