l=[1,2,3,4,5,6,7,8,9]
y=[]
"""
for i in l:
	if i%2==0:
		y.append(i)
print(y)
"""
y=[ i for i in l if i%2==0]
print(y)