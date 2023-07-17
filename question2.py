s=input("Enter input string : ")

freq={}

for x in s:

    if x in freq:

       freq[x]=freq[x]+1

    else:

       freq[x]=1

print("Frequency of each letter in the string : ")

print(freq)