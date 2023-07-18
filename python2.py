aString = input("enter string: ")
count1 = {letter: aString.count(letter) for letter in aString}
print(f"letter count: {count1}")