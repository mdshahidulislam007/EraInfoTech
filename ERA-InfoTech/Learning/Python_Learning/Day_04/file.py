stringMatch = "Palash"
with open('myFile.txt','r') as file:
    for str in file:
        if stringMatch in str:
            print("matched")
            break

input("Press enter to exit")
