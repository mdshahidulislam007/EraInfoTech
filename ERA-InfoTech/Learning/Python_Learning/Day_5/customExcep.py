class Error(Exception):
    pass

class ValueSmallError(Error):
    pass

class ValueLargeError(Error):
    pass


age=30

while True:
    try:
        a=int(input("Please Guess the Age: "))
        if a<age:
            raise ValueSmallError
        elif a>age:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("This value is small than the Age, Try Again!!!")
        print()
    except ValueLargeError:
        print("This value is Larger than the Age, Try Again!!!")
        print()
print("Congratulations!! You guessed it correctly")


#input("Press Enter to exit")
