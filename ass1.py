#Q.1)WAP to get factorial of a number using while loop.

number = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print("Factorial of", number, "is", factorial)
