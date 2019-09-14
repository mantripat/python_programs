import csv
with open('emp.txt','w',newline="") as j:
	w=csv.writer(j)
	w.writerow(['Empid','Name','Salary','Dept'])
	n=int(input("How many employees?"))
	for i in range(n):
		empid=input("Enter id:  ")
		ename=input("Enter name: ")
		esal=input("Enter salary: ")
		edept=input("Enter Dept: ")
		w.writerow([empid,ename,esal,edept])