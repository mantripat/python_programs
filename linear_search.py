l=[10,20,30,40]
key=int(input("Enter the element u want to search:"))
if key in l:
	print("Element found at loc:", l.index(key))
else:
	print("Element not in List")
