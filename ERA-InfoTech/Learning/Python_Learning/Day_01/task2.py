#Question 2: Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number
#solution:

start=int(input("Please enter range start number: "))
end= int(input("Please enter range end number: "))
print('Sum of current and previous number: ')
previous = 0
for start in range(start,end):
    sum = previous + start
    print(sum)
    previous=start

input('Press Enter to Exit')
