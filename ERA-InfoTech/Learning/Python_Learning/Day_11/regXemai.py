import re
class EmailValidation:

    def validate(self,email):
        ex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(ex,email):
            print('Email Is Valid')
        else:
            print('Email is invalid')

obj= EmailValidation()
while(True):
     n=input("Please input your email:")
     obj.validate(n)
