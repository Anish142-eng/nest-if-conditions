i = input("Enter if you have a medical cause: Y or N")

x = int(input("Enter your atendence: "))
if(i == "Y" or x > 75):
    print("Your accepted")
else:
    print("Not accepted")    