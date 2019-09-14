# i/p=A2B3  o/p=ACBE using ASCII
a="A2B3P2"
b=""
print("input string=",a)
for i in range(len(a)):
	if a[i].isdigit():		
		x=int(a[i])
		c=(ord(a[i-1]))
		b+=str(a[i-1])+chr(c+x)		
print("final output",b)