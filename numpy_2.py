import numpy as np
city=['Hyderabad', 'Pune', 'Delhi']
l=np.arange(45).reshape(3,5,3)
for i in range(3):
	print(city[i])
	print(l[i])
print("Hyderabad price og G, S and P")
print(l[0,0:,])

"""
print("gold price for Hyd, Delhi, Pune")
print(l[0:,0:,])
"""

