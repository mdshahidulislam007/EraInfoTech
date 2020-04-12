#range
print(list(range(0, 10, 2)))


#Strings
str='bangladesh'
print(str[0])
print(str[-1])
print(str[3:7])
print(str[3:-3])
#del str
#string concate
str1='Hello '
str2='World'
print(str1*2+str2)
str3='hello ''world'
print(str3)
#iteration through loop
count=0
for letter in str:
    if letter=='a':
        count+=1
print('Number of "a" in bangladesh',count)

#String Membership Check
b='glad' in str
print(b)

# enumerate() function in string
print(list(enumerate(str)))

# len() function in string
print('length of "Bangladesh":',len(str))