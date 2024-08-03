sum = 0
arr = input().split()
a, b = int(arr[0]), int(arr[1])
if a <= b:
    for i in range(a, b+1):
        if i % 2 == 0:
            sum += i
else:
    for i in range(b, a+1):
        if i % 2 == 0:
            sum += i
print(sum)