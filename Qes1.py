s=input("Enter the string : ")
count=0
#b=len(s)
for i in range(0,len(s)):
    if(s[i]==" "):
        count+=1

print(len(s)-count)