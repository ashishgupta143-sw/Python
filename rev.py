#Wap to reverse a number inputNum=123   ExpectedOutput=321

n=int(input("Enter a number"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print("The reverse is",rev)
    print("count of total number",rev)
'''
n=123
'''
