x="I love python123, python is python"
#print(x.index("python"))


f='python'
j=0
pos=-1
while True:
	for i in range(3):
		pos=x.find(f[i],pos+1,len(x))
	if pos==-1:
		break
	print("Item at loc= ", pos)
	j=1
if j==0:
	print("item not found")		

