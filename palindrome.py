
#s1=input("enter any string to check if it is palindrome:")
"""
s1="maddsam"

print("reverse string=",s1[::-1])

if s1[0:]==s1[::-1]:
	print("String is palindrome")
else:
	print("Its not plaindrome")
"""
s="hi ! my name is Alpha ..... u can write it like @lph@ 123%%%6&8^%$#"
s2=""
for i in range(len(s)):
	if s[i].isalnum() or s[i].isspace():
		s2+=s[i]
print("new string is \t", s2)