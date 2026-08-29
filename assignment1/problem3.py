# Simple Calculator and Area Calculation

print("1. Simple Calculator")
print("2. Area of Rectangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    area = length * breadth

    print("Area of Rectangle =", area)

else:
    print("Invalid Choice")
   
 #sample output for choice 1
 #1. Simple Calculator
#2. Area of Rectangle
#Enter your choice (1 or 2): 1

#Enter first number: 20
#Enter second number: 10

#Addition = 30.0
#Subtraction = 10.0
#Multiplication = 200.0
#Division = 2.0

#sample output for choice 2

#1. Simple Calculator
#2. Area of Rectangle
#Enter your choice (1 or 2): 2

#Enter length: 12
#Enter breadth: 5

#Area of Rectangle = 60.0