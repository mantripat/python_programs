a="I love python, python is an easy,python is base for ML"
loc=-1
f={-1}
x=0
for i in range(loc+1,len(a)):
	loc=a.find("python",loc+1,i)
	if(loc!=-1):
		f.add(loc)
		x+=1
	elif loc==-1:
		x=0

if x!=0:
	f.remove(-1)
	print("Item found at loc:\t",f)
else:
	print("item not find")
