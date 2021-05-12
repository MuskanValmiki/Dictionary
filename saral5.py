list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
e={}
i=0
while i<len(list1):
    e[list1[i]]=list2[i]
    i+=1
print(e)
