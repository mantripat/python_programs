from functools import *
n_list=[1,2,3,4]
sum=0
#x=(reduce(lambda num1,num2:(num1+num2)/len(n_list),n_list))
#print(x)
x= reduce(lambda num1,num2:max(num1,num2),n_list)
print(x)
