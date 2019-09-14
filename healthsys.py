import os
import csv
import time
print("Old Patient or New Paient?....")
print("\t'1' for Old Patient")
print("\t'2' for New Patient")
p_type=int(input("Write your option here..."))
path="E:\\MyPythonProgram\\HealthCare\\"

if p_type==2:
	p_name=input("Enter New patient's name:")
	try:
		os.mkdir(path+p_name)
	except:
		print("Cannot create file, Patient name already exists")
		exit()
elif p_type==1:
	
	old_list=os.listdir("E:\\MyPythonProgram\\HealthCare")
	print(old_list)
	try:
		p_name=input("Choose patient's name:")
		if p_name in old_list:
			print("Welcome...")
		else:
			print("name not find") 
		
		
	except:
		print("This patient's does not exist:")
		exit()
else:
	print("Oops! You entered wrong input")
	exit()
x=time.ctime()
type=int(input("enter file number: '1' for diet and '2' for exercise"))
if type==1 :
	try:
		cpath=path+p_name+"\diet.txt"
		print("Enter data into diet.txt")
		with open(cpath,'a+',newline="") as j:
			w=csv.writer(j)
			w.writerow(['Date and Time','Meal'])
			p_meal=input("Enter food: ")
			w.writerow([x,p_meal])
	except FileNotFoundError as msg:
		print("Error Detected",msg)
	except:
		print("Unknown Error")
elif type==2:
	try:
		cpath=path+p_name+"\exec.txt"
		print("Enter data into exercise.txt")
		with open(cpath,'a+',newline="") as j:
			w=csv.writer(j)
			w.writerow(['Date and time','Exercise'])
			p_exec=input("Which exercise u did? : ")
			w.writerow([x,p_exec])
	except FileNotFoundError as msg:
		print("Error Detected",msg)
	except:
		print("Unknown Error")
else:
	print("You entered wrong file number")
