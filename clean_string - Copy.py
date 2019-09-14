## clean this list and result should be double of the integers in list
x="10,20,30"
y=''
for i in x:
	if i in '0123456789':
		y+=i
print(int(y)*2)
