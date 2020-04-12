class Parent:
    
    def __init__(self,fname,lname,bname):
        self.fname=fname
        self.lname=lname
        self.bname=bname

class Student(Parent):
    
    name=''
    

    def __init__(self,name):
        
        super().__init__('Abul Kalam','Azad','Jafor Iqbal')
        print('Student Name is :',Person.fname)
        self.name=name
        

    def display(self):
        print('Student Name is :',self.name)
        
       
      #  print('Student Parent Last Name is :',Parent.fname)
      #  print('Student Brother Name is :',brother_name)
        


#p = Parent('Abul Kalam','Azad','Jafor Iqbal')
#print(p.fname)
s = Student('Towfiq')
s.display()
