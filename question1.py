Input=input("Enter a string : ")
count=0
for word in Input.split(' '):
    count=count+1
print(f"The number of words in the input string is {count}")