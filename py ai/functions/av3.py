def add(P, Q):
    return P + Q 
def subract(P, Q):
    return P - Q 
def multiply(P, Q):
    return P * Q 
def divide(P, Q):
    return P / Q 
print("please select the operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("please end your choice (a/ b/ c/ d/): ")
num_1 = int (input("enter 1st num: "))
num_2 = int (input("enter 2st num: "))
if choice == 'a':
    print(num_1, "+", num_2," = ", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2," = ", subract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2," = ", multiply(num_1, num_2))        
elif choice == 'd':
    print(num_1, "/", num_2," = ", divide(num_1, num_2))  
else:
    print("invalid")