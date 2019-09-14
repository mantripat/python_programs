num=int(input("enter any decimal number"))
i=0
j=0
s=[]
st=""
rem=0
q=0
dict={10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} 
while(num>1):
	rem=int(num%16)
	num=num/16
	if rem in dict:
		rem=dict[rem]
	s.append(rem)
	i=i+1
print(s)
for x in s:
	st+=str(x)
print("new string reversed=", st[::-1])