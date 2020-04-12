class Employee:
    name=''

    def __init__(self,n):
        self.name=n

    def __call__(self,n):
        self.name=n
        
    def __len__(self):            
        return len(self.name)

e = Employee('Shahidul')   #by __init__
print(e.name)
print('Employee Name length: ',len(e))    #if __len__ exist in class then len() works ,otherwise error

# the __init__ method is used when the class is called to initialize the instance
# the __call__ method is called when the instance is called


e('Palash')    #by __call__
print(e.name)
print('Employee Name length: ',len(e))
