import re
class MobileValidate:

    def validate(self,mobile):
        ex='\A01(3|4|5|6|7|8|9)\d{8}$'

        if re.search(ex,mobile):
            print('Number is Valid')
        else:
            print('Number is Invalid')

obj = MobileValidate()

while(True):
    n=input('Please Enter Your Number:')
    obj.validate(n)
