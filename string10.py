# i/p=ABCBAB123 o/p= it is alphnumeric
a=input("Enter any string")
num1=""
c1=0
c2=0
c3=0
print("input string=",a)
if a.isalnum():
	if a.isalpha():
		if a.islower():
			print("String is Alphabets and Lower")
		elif a.isupper():
			print("String is Alphabets and Upper")
	elif a.isdigit():
		print("Digits Only")
	else:
		print("Alphanumeric")

elif a.isspace():
	print("Space Only")
else:
	print("Contains Spl chars")


	
"""	
if a.isdigit(): 	
	print("String is Numeric")
elif a.isalpha(): 	
	print("String is Alphabetic")
elif a.isalnum():
	print("String is Alphanumeric")

else:
	print("String contains symbol")
"""