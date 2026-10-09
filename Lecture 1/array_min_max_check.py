#Create arraycls and find min and max
arr = [6,8,20,25,10,16,9]
max = arr[0]
min = arr[0]
s_max = arr[0]
s_min = arr[0]
for i in range(0,len(arr)):
    if arr[i] > max:
        s_max = max
        max = arr[i]        
    if arr[i] < min:
        s_min = min
        min = arr[i]
print(max)
print(min)
print(s_max)
print(s_min)