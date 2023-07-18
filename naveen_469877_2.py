a=input("Enter the sentence = ")
dict = { letter:a.count(letter) for letter in a }
print(dict)