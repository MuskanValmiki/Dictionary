# datas= [{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,"school":"Union"},{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
# for index in range(0,len(datas)):
#     for key  in datas[index]:
#         if datas[index]["score"]>50:
#             if datas[index]["school"]=="pyds":
#                 print(datas[index])
#                 break

datas= [{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,"school":"Union"},{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
i=0
c=0
while i<len(datas):
    for key in datas[i]:
        if datas[i]["score"]>50:
            if datas[i]["school"]=="pyds":
                if c==0:
                    print(datas[i])
                    c+=1
    i+=1

