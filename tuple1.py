t1=("Aditya",35,78,"O grade")
print(type(t1))
print(t1)

#tuple slicing
print(t1[1:])
print(t1[:3])
print(t1[1:3])


#find length of the tuple

print("The length of the tuple is",len(t1))

#you can also give negative indexing.
print(t1[-2])
print(t1[-1])



#Note: #List is a collection which is ordered and changeable.
#List Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable.
#Tuple Allows duplicate members.


t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)
