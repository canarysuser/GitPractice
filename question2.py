a=input("Write a line: ")
dict={}
for x in a:
    if(x in dict):
        dict[x]+=1
    else:
        dict[x]=1
print(dict)