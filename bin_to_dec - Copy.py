num=(input("enter any binary number"))
i=0
j=0
print("entered str is: ",num )
l=len(num)
print("length=", l)
s=num[::-1]
print("reverse of string is", s)
while(i<l):
	j=j+(int(s[i])*(2**i))
	i=i+1
print("Decimal equivalent", j)


