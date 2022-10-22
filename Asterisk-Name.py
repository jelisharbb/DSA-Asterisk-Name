# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

name = "JELI"
printJ = [[" " for i in range(5)] for j in range(5)]
printE = [[" " for i in range(5)] for j in range(5)]
printL = [[" " for i in range(5)] for j in range(5)]
printI = [[" " for i in range(5)] for j in range(5)]

# code for J
for row in range(5):
    for col in range(5):
        if (col == 0 and row == 3) or (row == 4 and (col != 0 and col != 4)) or (col == 4 and row != 4):
            printJ[row][col] = "*"

# code for E
for row in range(5):
    for col in range(5):
        if (row == 0 or row == 2 or row == 4) or (col == 0 or row == 1 and row == 3):
            printE[row][col] = "*"

# code for L
for row in range(5):
    for col in range(5):
        if (col == 0) or (row == 4 and col != 0):
            printL[row][col] = "*"

# code for I
for row in range(5):
    for col in range(5):
        if (col == 0):
            printI[row][col] = "*"

# print JELI
for i in range(5):
    for j in range(5):
        print(printJ[i][j], end = " ")
    print(end = "  ")
    for j in range(5):
        print(printE[i][j], end = " ")
    print(end = "  ")
    for j in range(5):
        print(printL[i][j], end = " ")
    print(end = "  ")
    for j in range(5):
        print(printI[i][j], end = " ")
    print()