
# 1.Using input function take two number and then swap the number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("value of a =", a)
print("value of b =:", b)









#3.Find the Simple Interest on Rs. 200 for 5 years at 5% per year


def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    
    si = (p * t * r)/100
    
    print('The Simple Interest is', si)
    return si
    
simple_interest(8, 6, 8)

 # 4. Create a Python program that checks
#whether a person is eligible to vote (18 years or older) based on their age.

age = int(input("Enter age : "))

if age >= 18:
    print("Eligible for Voting!")
else:
    print("Not Eligible for Voting!")
