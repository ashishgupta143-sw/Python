#Q.3)Write a while loop to calculate the sum of digits of a given number.

number = int(input("Enter a number: "))
sum1= 0

while number != 0:
    sum1 += number % 10
    number //= 10

print("Sum of digits:", sum1)
