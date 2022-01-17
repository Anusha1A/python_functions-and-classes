def list_to_dict(list1,list2):
	dict1 = {}
	for key in list1:
    		for value in list2:
        			dict1[key] = value
        			list2.remove(value)
        			break  
	print ("Resultant dictionary is : " +  str(dict1)) 
list1 = []
list2 = [] 
n=int(input("enter size for list1"))
m=int(input("enter size for list2"))
for i in range(n):
	a=input()
	list1.append(a)
for i in range(m):
	b=int(input())
	list2.append(b)

print ("Keys: " + str(list1))
print ("Values: " + str(list2)) 
  
list_to_dict(list1,list2)


