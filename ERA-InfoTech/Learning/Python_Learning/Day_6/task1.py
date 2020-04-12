import sys
try:
    f = open("myfile.txt", "w")
    f.write("Hello!! World")
   # f = open("myfile.txt", "r")
    print(f.read())
    
except:
    print("Opsss!!",sys.exc_info()[0],"occured.")
