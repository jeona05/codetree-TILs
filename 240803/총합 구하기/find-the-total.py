sum = 0
arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        sum += i
print(sum)