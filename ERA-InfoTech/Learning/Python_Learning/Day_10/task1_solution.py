#1
dict={}
n=int(input("Please Enter the Number of pair:"))
for i in range(n):
    name=input("Please Enter the Name:")
    mobile=input("Please Enter the Telephone number:")
    dict[name]=mobile

print('1)Resultant Dictionary is:',dict)

#2
for i in dict:
    if i=='Jane Doe':
        dict[i]='+27 555 1024'
        
print('2)Updated Dictionary is:',dict)

#3
dict.update( {'Anna Cooper' :'+27 555 3237'} )
print('3)Updated Dictionary is:',dict)

#4&5
flag=''
for i in dict:
    if i=='Tahashin':
        flag='True'
        break
    else:
       flag='False'
if flag=='True':
    print(dict['Tahashin'])
else:
    print("None")

#6
print('6)All the keys are:',dict.keys())

#7
print('7)All the values are:',dict.values())
