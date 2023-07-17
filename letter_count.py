aString=input("Enter the String :")
CountString={}
for x in aString:
    CountString[x]=aString.count(x)
print(CountString)