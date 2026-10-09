# Program to print plus sign star pattern

row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row):
        if i == row // 2 or j == row // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()