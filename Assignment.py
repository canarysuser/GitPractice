row=int(input('Enter the row'))
col=int(input('Enter the col'))
matrix=list()
for i in range(0,row):
    for j in range(0,col):
        matrix.append((i+1,j+1))
print(matrix)