sum = 0
num = 0
arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        num += 1
print(f"{sum} {sum/num:.1f}")