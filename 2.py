word = input("Enter the Input line")    
mp={ }
for x in word:
    if(mp.get(x,0)==0):
        mp.update({x:1}) 
    else:
        mp[x]+=1
mp.pop(" ")        
print(mp)            
 