#Program to check palindrome case for number 
num = int(input("Enter a number:"))
temp_num = num
rev_num = 0
while num != 0:
    rev_num = rev_num * 10 + (num % 10)
    num = num // 10
if rev_num == temp_num:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")