string = input(" Enter the string ")
letter = {letter:string.count(letter) for letter in string}
print(letter)