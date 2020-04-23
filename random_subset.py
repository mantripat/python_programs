from random import sample
list=[1,2,3,4,5,6,7,8,9,0]
print("Random sample will choose a subset from given list using random.sample(list_name, no of elements)")
print(sample(list,7))

from random import shuffle
print("List before shuffling",list)
shuffle(list)
print("Lisy after shuffling")
print(list)