
print((lambda x:x+1)(2))  
#lambda 2:2+1 =>3

add= lambda x:x+1   
print(add(2))

add= lambda x,y:x+y
print(add(2,2))

#lambda function as parameter in lambda function

myFunc=lambda x,anotherFun: x+ anotherFun(x)
print(myFunc(4,lambda x:x*x))   #here x=4, anotherFun = lambda x:x*x

#another way
print((lambda x,anotherFun: x+ anotherFun(x))(4,lambda x:x*x))

#for unknown number of parameters
print((lambda *arb: sum(arb))(1,2,3,4))
