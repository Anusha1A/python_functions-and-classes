def mergedict(dict_1,dict_2):
    dict_1.update(dict_2)
    print('Updated dictionary:')
    print(dict_1)

dict_1 = {}
dict_2 = {}
n=int(input("enter size"))
m=int(input("enter size"))
for i in range(n):
    key=int(input("enter key for dict1:"))
    values=int(input("enter value for dict1:"))
    dict_1[key]=values
for j in range(n):
    keys=int(input("enter key for dict2:"))
    value=int(input("enter value for dict2:"))
    dict_2[keys]=value
mergedict(dict_1,dict_2)
