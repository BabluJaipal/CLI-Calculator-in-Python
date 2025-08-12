def add(a,b):
    return a+b
def subs(a,b):
    return a-b
def multy(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Invalid, divide by zero error !"
    return a / b
def inpt():
    print("\nEnter accordingly ")
    print("Enter 1 for addition: ")
    print("Enter 2 for Subtraction: ")
    print("Enter 3 for multiplication: ")
    print("Enter 4 for division: ")
    print("Enter 5 for Exit: ")

def main():
    while True:
        inpt()
        choice = input("Enter Your choice: ")

        if choice == "5":
            print("Exiting....Please wait !")
            break
            
        if choice in ["1","2","3","4"]:
            try:
                num1 = int(input("Enter Your first value: \n"))
                num2 = int(input("Enter you second value: \n"))

                if choice == "1":
                    print("\n Result of  addtion is: ",add(num1,num2))
                elif choice == "2":
                    print("\n Result of Subtraction is: ",subs(num1,num2))
                elif choice == "3":
                    print("\n Result of  Multiplication :",multy(num1,num2))
                elif choice == "4":
                    print("\n Result of  Division is: ",divide(num1,num2))

            except ValueError:
                print("Sorry! Try Again, You are enteres wrong value anywhere!")
        
        else:
            print("Enter Correct input 1-5 ")

main()
            
            
