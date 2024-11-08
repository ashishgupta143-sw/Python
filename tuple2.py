'''

Unordered: Unordered means that the items in a set
do not have a defined order.
Set items can appear in a different order every time
you use them, and cannot be referred to by index or key.
Unchangeable: Set items are unchangeable, meaning that
we cannot change the items after the set has been created.
Note: Once a set is created, you cannot change its items,
but you can remove items and add new items.
Duplicates Not Allowed:
Sets cannot have two items with the same value.

'''
thisset = {"apple","banana","cherry","apple"}

print(thisset)
thisset = {"apple","banana","cherry",True,1,2}

print(thisset)
print(len(thisset))

set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

weekdays={"Sun","Mon","Tue","wed","thurs","fri"}

