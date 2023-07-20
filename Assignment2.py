n=int(input("Enter a Number: "))

ones=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

hundred=["","", "twenty","Thirty", 'Fourty', "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]

tens=["Ten","Eleven","Twelve", "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]




if n>99999:

    print("Cannot be Written")

else:

    theList=[0,0,0,0,0,0]

    i=0

    while n>0:

        theList[i]=n%10

        i+=1

        n=n//10

    num=" "

    if theList[4]!=0:

        if(theList[4]==1):

            num+=tens[theList[3]] + " Thousand "

        else:

            num+=hundred[theList[4]]+" "+ ones[theList[3]]+ " Thousand "

    else:

        if theList[3]!=0:

            num+=ones[theList[3]]+ " Thousand "

    if theList[2]!=0:

        num+=ones[theList[2]]+ " Hundred "

    if theList[1]!=0:

        if(theList[1]==1):

            num+=tens[theList[0]]

        else:

            num+=hundred[theList[1]]+" "+ ones[theList[0]]

    else:

        if theList[0]!=0:

            num+=ones[theList[0]]




    print(num)