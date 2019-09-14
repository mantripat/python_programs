# i/p=A1B2C3 o/p=ABC123

a=input("enter any alphanumric string")
alp=""
num=""
f=""
print("input string=",a)
for i in range(len(a)):
	if a[i].isdigit():		
		num+=a[i]
	else:
		alp+=a[i]
	f=alp+num
		
print("final output",f)