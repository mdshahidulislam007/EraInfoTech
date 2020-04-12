#1: Suppose we want to create an output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values. Let’s see how to do this using for loops and dictionary comprehension.

#solve using for loop

myDict={1,2,3,4,5}
resultDict={}

for x in myDict:
    if x%2 !=0:
        resultDict[x]=x**3
print("Using 'For loop' Output Dictionary Is: ",resultDict)

#solve using list comprehension

result={ i:i**3 for i in myDict if i%2!=0}
print("Using 'List Comprehension' Output Dictionary Is: ",result)
