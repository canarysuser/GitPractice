# Ques1 Write a Python script to collect input from the user. The script should count the number of words in the list.
a=input("Enter the String: ")
cnt=0
b=len(a)
for x in range (0,b):
    if a[x]=='':
        cnt+=1
    #print(cnt)

print("count of words is:" ,b-cnt)