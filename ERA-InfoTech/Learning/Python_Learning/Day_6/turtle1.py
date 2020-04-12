import turtle
def myFun(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

n=int(input("Please Enter the length of the triangle: "))
myFun(n)
