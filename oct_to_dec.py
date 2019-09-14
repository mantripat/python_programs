num=(input("enter any oct number"))
i=0
j=0
print("entered str is: ",num )
l=len(num)
s=num[::-1]
st=[]
print("reverse of string is", s)
while(i<l):
	j=j+(int(s[i])*(8**i))
	i=i+1
print("Decimal equivalent", j)

