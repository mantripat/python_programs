num=int(input("enter any decimal number"))
i=0
j=0
s=[]
st=""
rem=0
q=0
while(num>1):
	rem=int(num%8)
	num=num/8
	s.append(rem)
	i=i+1
print(s)
for x in s:
	st+=str(x)
print("new string reversed=", st[::-1])