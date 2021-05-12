car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
user=input("enter any key=")
if user in car:
    del car[user]
    print(car)
else:
    print(car)
# delete key in dictanary
