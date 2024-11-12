def main():
    #variables and operators
    itemPrice = float(input("Enter the item price: "))
    itemAmt = int(input("how many items do you want to buy"))
    itemTax = itemPrice * 0.2
    totalPrice = itemAmt * (itemPrice + itemTax)
    print("Tax on the item is", itemTax)
    print("Total item price is", totalPrice)

    #an if statement
    year = int(input("Enter the year you were born: "))
    if year % 4 == 0:
        print("You were born in a leap year")
    else:
        print("you were not born in a leap year")
    if year == 2004:
        print("you were born in the same year as me yipee!!")
    elif year > 2004:
        print("you are younger than me")
    else:
        print("you are older than me!!!")

    #A Common Error: Integer divided by Integer (Dynamic typing to the rescue…)
    half = 1.0/2.0
    print(type(half)) 
    print(f"One half (1/2) = {half}")

    #fahrenheit to celsius
    celsius = int(input("enter celsius temp to be converted"))
    converted = celsius * (9/5) + 32
    print(celsius, "C = ", converted, "F")

    #currency Conversion
    quidIN = float(input("Input the amount of pounds youd like to convert"))
    rate = float(input("enter the conversion rate"))
    converted = quidIN * rate
    print("converted amount is: ", converted)

    cVal = float(input("input amount to be converted"))
    uChoice = float(input("press 1 to convert £ to $ or 2 for $ to £"))
    if uChoice == 1:
        cVal * 1.5
    else:
        cVal / 1.5
    print("converted amount", cVal)
    
    #maximum number
    one = int(input("input value 1"))
    two = int(input("input value 2"))
    three = int(input("input value 3"))
    four = int(input("input value 4"))
    five = int(input("input value 5"))

    max = 0
    if one > max:
        max = one
    if two > max:
        max = two
    if three > max:
        max = three
    if four > max:
        max = four
    if five > max:
        max = five
    print("biggest number is:", max)




if __name__ == '__main__':
    main()