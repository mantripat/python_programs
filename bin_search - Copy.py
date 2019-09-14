# Binary Search using List

l=[2,4,6,8,11,13,15,17,20,22]
print(l)
item=int(input("Enter element u want to search"))

start=0
end=len(l)-1
while(start<=end):
	mid=(start+end)//2
	if item==l[mid]:
		print("Item Found at::",mid)
		break
	else:
		if item<l[mid]:
			end=mid-1
		else:
			start=mid+1
