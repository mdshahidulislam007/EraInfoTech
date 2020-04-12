
class Student:
    name=''
    rollNo=''
    dept=''
    email=''
    payment=''

    def __init__(self,name,rollNo,dept,email,payment):
        self.name=name
        self.rollNo=rollNo
        self.dept=dept
        self.email=email
        self.payment=payment

    def display(self):
        print('Student Name is:',self.name)
        print('Student Roll No is:',self.rollNo)
        print('Student Department is:',self.dept)
        print('Student Email is:',self.email)
        print('Student Montly fee is:',self.payment)
        

s = Student('Shahidul',31,'CSE','mdshahidul.cse007@gmail.com',500)        
s.display()
