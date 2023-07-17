dic={}
ent=input("enter:")#Hello
for i in ent:
    if i in dic:
        dic[i]+=1
    elif i==" ":
        pass
    else:
        dic[i]=1
print(dic)
