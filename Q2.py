#2. Write a script to get input line from the user and count the occurences of each letter in the line.
a=input("input: ")
b={}

for i in a:
    if i==' ':
        continue
    if i in b:
        b[i]+=1   
    else:
        b[i]=1     
print(b)
    
