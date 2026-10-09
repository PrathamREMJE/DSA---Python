#Program to print descending triangular number constant pyramid

row = int(input("Enter number of rows:"))
cols = int(input("Enter number of cols:"))

for i in range(1,row+1):
    for j in range(cols,i-1,-1):
        print(j,end=" ")
    print()

