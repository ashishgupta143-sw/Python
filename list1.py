#List is a collection which is ordered and changeable
#Allow duplicate members.

mylist=["Oil", "Soap",123, "Oil","kurkure","Dairymilk"]
print (mylist)
print (type (mylist))
print (mylist[0])

#slicing list elements

print(mylist[1:])
print(mylist[2:5])

#You can use negative index as well
print(mylist[-1])
print(mylist[-2])
for i in mylist:
    print(i,end=" ")
