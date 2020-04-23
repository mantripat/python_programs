list=['apple','mango','orange','grapes','papaya']
from random import choice
from random import seed
print("Output Before using seed in random choice")
print(choice(list), choice(list),choice(list),choice(list))
seed(7)
print("Output After using seed in random choice")
print(choice(list), choice(list),choice(list),choice(list))

from random import choices
print("using choices method")
print(choices(list,k=8))