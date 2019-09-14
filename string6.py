# i/p= "A2B3" o/p="AABBB"
a="A2B3CD5"
b=""

"""
print("input string=",a)
for i in range(len(a)+1):
	if a[i].isdigit():		
		x=int(a[i])
		a=a.replace(str(x),str(a[i-1]*int(x-1)))
		
print("final output",a)

"""
for i in a:
	if a[i].isdigit():
		b=a[i]