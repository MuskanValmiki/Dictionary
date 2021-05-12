dict =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
count=0
for i in dict:
    for keys in dict[i]:
        count+=1
print("total count",count)
# count the keys values,total count 5
