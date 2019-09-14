"""
x=['22-08-2012','23-08-2012','24-08-2012']
s=""
s1=""
l=[]
l2=[]
for i in range(len(x)):
	s=x[i]
	s=s.split("-")
	l.append("/".join(s[::-1]))
	y=l[i][0:5]
	m=l[i][4:7]
	d=l[i][8:10]
	l[i]=y+d+m

print(l)

"""
l=['22-08-2012','23-08-2012','24-08-2012']
f=[]
for i in l:
	z=[0,0,0]
	y=i.split("-")
	z[0]=y[2]
	z[1]=y[1]
	z[2]=y[0]
	f.append("/".join(z))
print(f)
