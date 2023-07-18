sentence = input("Enter a sentence: ")
lcount = {}
for x in sentence:
    lcount[x] = sentence.count(x)
print(lcount)