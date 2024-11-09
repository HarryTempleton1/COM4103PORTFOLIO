import math

def main():
    #initialises the menu input variable before the while loop starts so the program does not crash because of a variable being used before it is assigned
    menuInput = 0
    #when 9 is input the program will end
    while(menuInput != 9):
        print("SCIENTIFIC CALCULATOR")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5. EXPONENTIATION")
        print("6. SQUARE ROOT")
        print("7. LOGARITHM")
        print("8. TRIGONOMETRIC FUNCTIONS")
        print("9. QUIT")
        menuInput = int(input("input a number to choose Operation or input 9 to leave"))
        #sends the flow of code to the function for the math type chosen
        if(menuInput == 1):
            addition()
        elif(menuInput == 2):
            subtraction()
        elif(menuInput == 3):
            multiplication()
        elif(menuInput == 4):
            division()
        elif(menuInput == 5):
            exponentiation()
        elif(menuInput == 6):
            squareRoot()
        elif(menuInput == 7):
            squareRoot()
        elif(menuInput == 8):
            logarithm
        #if any other integers are input it will default to this else staterment showing an invalid input
        else:
            print("invalid input")

def addition():
    inpA = int(input("input the first number you would like to add"))
    inpB = int(input("input the second number you would like to add"))
    result = inpA + inpB
    print(result)

def subtraction():
    
    inpA = int(input("input the number you want to be subtracted from"))
    inpB = int(input("input the number you want to subtract"))
    result = inpA - inpB
    print(result)
    

def multiplication():
    inpA = int(input("input the first number you would like to multiply"))
    inpB = int(input("input the second number you would like to multiply"))
    result = inpA * inpB
    print(result)

def division():
    inpA = int(input("input the number you want to be divided"))
    inpB = int(input("input the number you want to be divided by"))
    #error checking to prevent divide by zero
    if inpA or inpB == 0:
        print("invalid input")
    else:
        result = inpA / inpB
        print(result)

def exponentiation():
    inpA = int(input("What would you like to raise E to the power of?"))
    result = math.exp(inpA)
    print(result)

def squareRoot():
    inpA = int(input("What number would you like to squareroot?"))
    #sqrt is the syntax for the square root function in the math library
    result = math.sqrt(inpA)
    print(result)

def logarithm():
    inpA = int(input("What number would you like to find the logarithm of"))
    inpB = int(input("What number do you want the base of the logarithm to be (leave blank for E)"))
    #inpA is the number the logarithmic function is working on and inpB is the base of the log
    result = math.log(inpA, inpB)
    print(result)

def trigonometricFunctions():
    print("Which trigonometric function would you like to select?")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    print("4. Main Menu")
    menuInput = int(input("input a number to choose Operation or input 9 to leave"))
    if(menuInput == 1):
        sine()
    elif(menuInput == 2):
        cosine()
    elif(menuInput == 3):
        tangent()
    elif(menuInput == 4):
        main()

def sine():
    inpA = int(input("What number would you like to sine?"))
    result = math.sin(inpA)
    print(result)

def cosine():
    inpA = int(input("What number would you like to cosine?"))
    result = math.cos(inpA)
    print(result)

def tangent():
    inpA = int(input("What number would you like to tangent?"))
    result = math.tan(inpA)
    print(result)


if __name__ == '__main__':
    main()