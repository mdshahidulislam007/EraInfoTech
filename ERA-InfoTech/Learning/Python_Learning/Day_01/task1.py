#Question 1: Accept two int values from the user and return their product. If the product is greater than 1000, then return their sum
#Solution:

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
product = num1*num2
if product>1000:
    print("The sum is: ",num1+num2)
else:
    print("The result is:",product)

input('Press ENTER to exit')
