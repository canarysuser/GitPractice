lst = []
c = 1
lst = input("enter the script")
print(lst)
for i in lst:
    for j in i:
        if(j == " "):
            c += 1
print(c)


