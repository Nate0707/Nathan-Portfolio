#Nathan Gonzalez
#Simple Calculator

#Init

#Functions
#Adds num + num2 and prints the results
def add (num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))

def subtract (num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))

def multiply (num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))

def divid (num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))
#Main
def calculator():
    print("Welcom Preschoolers to Simple Calculator")
    while True:
        print(" Please choose an operation: ")
        print("""1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Quit""")
        operation = int(input("(1-5 :"))
        if operation == 1:
            add1 = int(input("Eter first number: "))
            add2 = int(input("Eter second number: "))
            add(add1,add2)

        elif  operation == 2:
            subtract1 = int(input("Eter first number: "))
            subtract2 = int(input("Eter second number: "))
            subtract(subtract1,subtract2)

        elif operation == 3:
            multiply1 = int(input("Eter first number: "))
            multiply2 = int(input("Eter second number: "))
            multiply(multiply1,multiply2)

        elif operation == 4:
            divid1 = int(input("Eter first number: "))
            divid2 = int(input("Eter second number: "))
            divid(divid1,divid2)

        elif operation == 5:
            print("Goodbye")
            break
calculator()
