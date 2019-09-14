availableExits=[]
direction=""
locations={0:"u r in front of laptop:",
        1:"u r standing in front of Road",
	2:"u r on top of Hill ",
	3:"u r inside a Building",
	4:" u r in a Valley", 
	5:"u r in Forest"}
exits=[{"Q":0},
	{"W":2, "E":3,"N":5, "S":4,"Q": 0},
	{"N":5, "Q": 0},
	{"W":1, "Q":0}, 
	{"N":1, "w":2, "Q":0},
	{"w":2, "S":1, "Q":0}]
loc=1
while True:
	availableExits=",".join(exits[loc].keys())
	print(locations[loc])
	if loc==0:
		break
	print("Available exits are: ", availableExits)
	direction= input("enter any direction: ").upper()
	print()
	if direction in exits[loc]:
		loc=exits[loc][direction]
	else:
		print("u cannot go in that direction")
print("Bye!")		