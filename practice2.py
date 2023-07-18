mp = {}
lst = input("Enter string: ")

for s in lst:

    if s!= ' ':

        if s not in mp:

            mp[s]=1

        else:

            mp[s]=mp[s]+1




print(mp)