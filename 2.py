line=input("enter the line:")
mp={ }
for x in line:
    if(x==" "):
        continue
    if(mp.get(x,0)==0):
        mp.update({x:1})
    else:
        mp[x]+=1
print(mp)