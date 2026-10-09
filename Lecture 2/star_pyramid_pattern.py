# Program to print star pyramid pattern

row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()