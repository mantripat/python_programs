"""
x=3
for i in range(1,6):
	print("  "*(5-i), end=" ")
	for j in range(0,i):
		print(x+i,"  ",end=" ")		
	print()

x=2


x=range(1,4)
for i in range(1,6):
	##print("  "*(5-i), end=" ")
	for j in range(1,i+1):
		print(j,end=" ")		
	print()
for i in range(1,6):
	print("  "*(5-i), end=" ")
	for j in range(0,i):
		print(x[j],end=" ")		
	print()
"""
x=[]
np=[]
for i in range(3,15):	
		if i%i!=0:
			x.append(i)
		else:
			##print("non prime")
			np.append(i)

print("new list=",x)
print("non prime list=",np)
