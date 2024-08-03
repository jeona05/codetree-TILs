sum = 0
n = int(input())
for _ in range(n):
    a = int(input())
    sum += a
print(f"{sum} {sum/n:.1f}")