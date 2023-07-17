# 1st Question

inp = input("Enter Something : ").split(" ")
print(len(inp))



# 2nd Question


inp = input("Enter something : ")
dict = {}
for i in inp:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)