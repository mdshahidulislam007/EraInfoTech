import sys

anyList=['a','0','2']
for entry in anyList:
    try:
        print("The Entry is: ",entry)
        r=1/int(entry)
        break
    except:
        print("Opsss!!",sys.exc_info()[0],"occured.")
        print("Next Entry Please")
        print()
print("The receprocal of ",entry," is: ",r)

input("Press enter to exit")

