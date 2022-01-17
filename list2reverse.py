def list2reverse(list1,list2):
	for x, y in zip(list1, list2[::-1]):
    		print(x, y)
list1 = []
list2 = []
n=int(input("enter size for list1"))
m=int(input("enter size for list2"))
for i in range(n):
	a=int(input())
	list1.append(a)
for i in range(m):
	b=int(input())
	list2.append(b)
list2reverse(list1,list2)

