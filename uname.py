import time
import os
u='123'
p='321'
u=input("Enter username::")
c=0
if u=='123':
	p=input("Enter Password")
	while(p!='321'):
		c+=1
		if c!=2:
			p=input("Reneter Password::")
		else:
			print("More than Two Attempts")
			for i in range(10,0,-1):
				print("Come Back After",i,"secs...")
				time.sleep(1)
				os.system('cls')

			break
	else:
		print("Welcome to My Screen")
else:
	print("Username Invalid")	