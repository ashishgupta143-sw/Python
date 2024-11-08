# Accept age of child and make a decision whether he is eligible for play group, Nursery, Jr.Kg or Sr.Kg

age = float(input("Enter the age of the child: "))

if   2 <= age < 3:
    print("you are eligible for Play Group.")
elif 3 <= age < 4:
    print("you are eligible for Nursery.")
elif 4 <= age < 5:
    print("you are eligible for Jr.Kg.")
elif 5 <= age < 6:
    print("you are eligible for Sr.Kg.")
else:
    print("you are not eligible for any of any classes.")
