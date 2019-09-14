num=int(input("enter any decimal number"))
i=0
j=0
s=[]
st=""
d=0
q=0
while(num>1):
	d=int(num%2)
	num=num/2
	s.append(d)
	i=i+1
print(s)
for x in s:
	st+=str(x)
print("new string reversed=", st[::-1])