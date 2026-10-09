#Program to check Armstrong case for number 

num = int(input("Enter a number:"))
temp_num = num
power = len(str(num))
sum = 0
while num != 0:
    sum += (num % 10)**power
    num = num // 10
if sum == temp_num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")