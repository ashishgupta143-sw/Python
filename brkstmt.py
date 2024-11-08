#use of break and continue

for i in range(1,21):
    if(i==10):
        break
    print(i)
print("---------------||----------")

#use of continue
for i in range(1,21):
    if(i==10):
        print("skipped")
        continue
    print(i)
