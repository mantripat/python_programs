num=(input("enter any Hex number"))
i=0
j=0
print("entered str is: ",num )
l=len(num)
s=num[::-1]
st=[]
print("reverse of string is", s)
dict={'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
while(i<l):
	if s[i] in dict:
		k=dict[s[i]]
		st.append(k)
	else:
		st.append(int(s[i]))
	j=j+(int(st[i])*(16**i))
	i=i+1
print("Decimal equivalent", j)

