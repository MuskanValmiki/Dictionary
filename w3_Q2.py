# add value to dict o/p=30
dict={0: 10, 1: 20}
sum=0
for i in dict:
    sum=sum+dict[i]
print(sum)

# add one key in dict o/p={ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}0: 10, 1: 20, 2: 30}
dict={0:10,1:20}
print(dict)
dict.update({2:30})
print(dict)
