num=input("enter any number")
i=0
sum=0
l=len(num)
print("length of string=", l)
while(i<len(num)):
	sum+= int(num[i])**3
	i=i+1

print("sum of digits=", sum)
if str(sum)==num:
	print("given number ",num, " is an Armstrong number")
else:
	print("Number is not Armstron")