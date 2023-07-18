line = input("Enter a line of text: ")
dic = {}
for x in line:
    if(x != " "):
        if(x in dic):
            dic[x]+=1
        else:
            dic[x] = 1

print(dic)