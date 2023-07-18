text = input("Write something: ")
letter = {letter:text.count(letter) for letter in text}
print(letter)