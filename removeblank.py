def remove_blank(list1):
	res = list(filter(None, list1))
	return(res)
list1=[]
n=int(input("enter size"))
for i in range(n):
	a=input()
	list1.append(a)
print(remove_blank(list1))
