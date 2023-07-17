s=input("enter the Name: ")
dict={}

for i in range(0, len(s)):
    if s[i] in dict.keys():
        dict[s[i]]+=1
    else:
        dict[s[i]]=1

print(dict)