# 2. Write a script to get input line from the user and count the occurences of each letter in the line. 
mp = {};
ss = input("enter word -> ");
for s in ss:
    if (s != ' '):
        if s not in mp:
            mp[s]=1;
        else:
            mp[s] = mp[s]+1;

print(mp)