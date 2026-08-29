

print("1. Prime Number")
print("2. Factorial")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    number = int(input("Enter a number: "))

    count = 0

    for i in range(1, number + 1):

        if number % i == 0:
            count = count + 1

    if count == 2:
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")

elif choice == 2:

    number = int(input("Enter a number: "))

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial =", factorial)

else:
    print("Invalid Choice")
    
    #sample output for choice 1
    ##1. Prime Number
    #2. Factorial
    #Enter your choice (1 or 2): 1
    #Enter a number: 5
    #5 is a Prime Number
    #
    
    #sample output for choice 2
    #1. Prime Number
    #2. Factorial
    #Enter your choice (1 or 2): 2
    #Enter a number: 5
    #Factorial = 120