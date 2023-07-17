inpstr = input("enter a string:")
charcount = {}
for ch in inpstr:
    if ch in charcount:
        charcount[ch]+=1
    else:
        charcount[ch]=1
print("character count:\n",charcount)
