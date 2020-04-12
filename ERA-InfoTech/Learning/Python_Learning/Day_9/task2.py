class Student:
    name=''
    rollNo=''
    dept=''
    email=''
    payment=''

    def display(self):
        print('Student Name is:',self.name)
        print('Student Roll No is:',self.rollNo)
        print('Student Department is:',self.dept)
        print('Student Email is:',self.email)
        print('Student Montly fee is:',self.payment)
        

s = Student()
s.name='Shahidul'
s.rollNo=31
s.dept='CSE'
s.email='mdshahidul.cse007@gmail.com'
s.payment=500
s.display()
