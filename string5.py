# i/p= "ABC" and "XYZ" o/p="AX"

s1="ABCP"
s2="XYZC"

output=""
i=j=0
while i<len(s1) or j<len(s2):
	if i<len(s1):
		output=output+s1[i]
		i=i+1
	if j<len(s2):
		output=output+s2[j]
		j=j+1
print(output)