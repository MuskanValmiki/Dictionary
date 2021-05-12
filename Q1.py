# key value and value  key change
a={1:"one",2:"two",3:"three",4:"four"}
a={value:key for key,value in a.items()}
print(a)

