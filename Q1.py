inp = input("enter the name : ")
dict ={ }

for i in range(0,len(inp)):
    if inp[i] in dict.keys():
        dict[inp[i]]+=1
    else:
        dict[inp[i]]=1

print(dict) 
