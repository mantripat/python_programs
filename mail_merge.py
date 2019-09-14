f=open ("msg.txt", 'r')
cdata=f.read()

with open('name.txt', 'r') as f:
	data=f.readlines()
	for i in data:
		n=i.split("\n")[0]
		txt='Hello' + n
		with open(n,'w') as t:
			t.write(txt)
			t.write('\n')
			t.write(cdata)