#Program to print descending triangular pyramid

row = int(input("Enter number of rows:"))
cols = int(input("Enter number of cols:"))

for i in range(cols,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

