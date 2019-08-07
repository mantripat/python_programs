i=int(input("Enter any number to check its divisibility by 5 and 8"))
if i%5==0 and i%8==0:
	print("Number is divisble by both 5 and 8")
elif i%5==0:
	print("number is divisible by 5 only")
elif i%8==0:
	print("number is divisible by 8 only")
else:
	print("Not divisible")
