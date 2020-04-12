import copy
x= [1,2,3]
z= copy.deepcopy(x)
print(x)
print(z)
x[0]='Shahidul'
print(x)
print(z)

