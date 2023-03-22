#Your Simple Calculator:
from ast import While

#Your Simple Functions
def Addition(a,b):
    answer = int (a) + int (b)
    print(str(a) + " + " + str(b) + " = " + str(answer) )
    
def Subtraction(a,b):
    answer = int(a) - int(b)
    print(str(a) + " - " + str(b) + " = " + str(answer))
    
def Multiply(a,b):
    answer = int(a) * int(b)
    print(str(a) + " x " + str(b) + " = " + str(answer))
    
def Divid(a,b):
    answer = int(a) / int(b)
    print(str(a) + " / " + str(b) + " = " + str(answer))
    
#Your Loop so your calculator run till you no longer need it
    
while True:

    print("\nA. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")
    print("E. Exit")

    Choice = input("\nLet's Calculate! ")

    if Choice == "a" or Choice == "A":
        print("Addition")
        a = input("Your Frist Number: ")
        b = input("Your Second Number: ")
        Addition(a,b)

    elif Choice == "s" or Choice == "S":
        print("Subtraction")
        a = input("Your Frist Number: ")
        b = input("Your Second Number: ")
        Subtraction(a,b)

    elif Choice == "m" or Choice == "M":
        print("Multiplication")
        a = input("Your Frist Number: ")
        b = input("Your Second Number: ")
        Multiply(a,b)

    elif Choice == "d" or Choice == "D":
        print("Division")
        a = input("Your Frist Number: ")
        b = input("Your Second Number: ")
        Divid(a,b)

    elif Choice == "e" or Choice == "E":
        print("Calculator Stopped")
        quit()
