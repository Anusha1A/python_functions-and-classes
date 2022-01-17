def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst
lst = []
n=int(input())
for i in range(n):
	a=int(input())
	lst.append(a)
print(Reverse(lst))
