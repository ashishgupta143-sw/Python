#Q.2)Write a while loop that counts the number of digits in a given number.

number = int(input("Enter a number: "))
count = 0

while number != 0:
    number //= 10
    count += 1

print("Number of digits:", count)
