

def fibonacci(num):

    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")
    
    #sampleoutput
    #Enter the number of terms: 7
    #Fibonacci Series:
    #0 1 1 2 3 5 8