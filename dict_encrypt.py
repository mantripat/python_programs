d={'A':'!', 'B':'@', 'C':'#', 'D':'$', 'E':'%',
 'F':'^', 'G':'&', 'H':'*', 'I':'(', 'J':')','K':'`', 'L':'~', 'M':'_', "N":'+', 'O':"="}
op=""
op2=""
ip=input("enter any String in CAPS to be encrypted..")
for i in range(len(ip)):
	if ip[i] in d:
		op+=d.get(ip[i])
		
	else:
		print("Character",ip[i]," not in Encryption list")

print("Encypted text is: ", op)
print()
ch=input("Press '1' for YES and '0' for NO  ")
if ch=='0':
	print("Bye!")
elif ch=='1':
	for i in range(len(op)):
		for k,v in d.items():
			if v==op[i]:
				op2+=k	
	print("Decrypted string is: ", op2)
else:
	print("Oops! You pressed wrong key!...")
		