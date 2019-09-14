"""
L=['python', 'Internetofthings', 'MAchineLeraninG']

x=len(L)
l=[]
print(x)

for i in range(len(L)):
	l.append(L[i].title())
print(l)
"""
l1=[]
s=""
l2=[]
l=['Anoop', 'is', 'good', 'girl']
for i in range(len(l)-1,-1,-1):
	l1.append(l[i])
print(l1)
for j in range(len(l1)):
	s=l1[j]
	l2.append(str(s[::-1]))
print(l2)