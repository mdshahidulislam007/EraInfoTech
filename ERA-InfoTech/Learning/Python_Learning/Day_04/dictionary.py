my_d={1:'Rose',2:'Belly','name':'john'}
print(my_d['name'])
print(my_d.get(2))    #by get()
my_d['name']='Ricky' #update
print(my_d)
my_d[3]='apple'  #new key:value assign
print(my_d)

print(my_d.pop(1)) #remove an item by pop() method
print(my_d)

#  my_d.clear()   #clean whole dictionary
#  del my_d     #for delating dictionary variable

new_d={x: x*x for x in range(9) if x%2==0}
print(new_d)
print(6 in new_d)
for i in new_d:
    print(new_d[i])