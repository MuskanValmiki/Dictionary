dic={'1':['a','b'], '2':['c','d']}
for key in dic:
    if key=="1":
        for i in dic[key]:
            for k in dic:
                if k=="2":
                    for j in dic[k]:
                        print(i+j)
# ac,ad,bc,bd
