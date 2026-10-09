# Program to print hollow diamond star pattern

row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(row - 2, -1, -1):    
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()