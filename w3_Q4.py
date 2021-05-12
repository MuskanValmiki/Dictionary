d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


d={1:10,2:20,3:30,4:40,5:50,6:60}
i=int(input("enter any key="))
if i in d:
    print(i,"is present in dictionary")
else:
    print(i,"is not present in dictionary")
