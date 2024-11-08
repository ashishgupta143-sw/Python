n=int(input("Enter a number"))
countdigit = len(str(inputNum))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print("The reverse is",rev)
    print("count of Digit",countdigit)
