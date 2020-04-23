from random import randint
from random import seed

#randint
seed(7)
print("Randint")
print(randint(0,9), randint(0,9), randint(1,9))
#randrange
from random import randrange

print("RandRange b/w -2 and 5=", randrange(-2,5))