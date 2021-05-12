fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')
print (len(fruit))
print(fruit) 
# 3
# {'Apple': 2, 'Banana': 1, 'apple': 1},count keys