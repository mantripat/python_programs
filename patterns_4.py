import random
x=int(random.random()*10)
for k in range(x,0,-1):
    print("  "*(x-k), end=" ")
    for l in range(0,k):
        print("*  ",end=" ")
    print()
