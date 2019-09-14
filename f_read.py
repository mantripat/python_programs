f=open("qw.txt",'r')

print("No. of lines: ", len(f.readlines()))
f.seek(0)
l=int(len(f.readlines()))
print("length=", l)
f.seek(0)
print("No. of characters : ", len(f.read()))
f.seek(0)

z=""
c=0
cd=0
z=f.read().split()
print(z)
c=len(z)
print("No. of words=", c)

dig=""
for i in range(c):
	for j in range(len(z[i])):
		if z[i][j].isdigit():
			dig=dig+z[i][j]
			cd+=1
		if z[i][j].isdigit()
	
print("list of digits=", dig)
print("no of digits= ", cd)
f.close