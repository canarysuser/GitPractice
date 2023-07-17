'''2. Write a script to get input line from the user and count the occurences of each letter in the line. '''

string = input("Enter a string: ")
count_dict = {}

for char in string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)