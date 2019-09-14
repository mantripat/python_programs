l1=[[1,2],[3,4]]
l2=[[5,6],[7,8]]
out=[]
print("List l1=", l1)
print("List l2=", l2)

"""
for i in range(len(l1)):
	out.append([])
	for j in range(len(l2)):
		out[i].append(l1[i][j]+l2[i][j])
print(out)
"""
out=[[l1[i][j]+l2[i][j] for j in range(len(l2))]  for i in range(len(l1))]
print(out)

