# i/p=ABCBABCBAC  o/p= count of 'A'=3, 'B'=2....
a="ABCABCAC"
num1=""
c1=0
c2=0
c3=0
print("input string=",a)
for i in range(len(a)):	
	if(a[i]=='A'):	
		c1=a.count(a[i])
	elif (a[i]=='B'):
		c2=a.count(a[i])
	elif(a[i]=='C'):
		c3=a.count(a[i])
print("final output for A B C =",c1,'\t',c2,'\t',c3,'\t')