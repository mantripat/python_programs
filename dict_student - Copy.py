d={'Rollno':["Name", "City", "Marks"],101:['Raj','chd',80.5], 102:['kaur','delhi',70.5]}

r=int(input("Enter Roll no."))
val=["name","city","percentage"]
l=[]
for i in range(len(val)):
	print("enter",val[i],end="")
	val1=input("  ..")
	l.append(val1)
	
print(l)
if r in d:
	print("This roll no already exists..")
else:
	print("Dictionary updated...")
	d.setdefault(r,l)
for k,v in d.items():
	print(k,"\t",v)
