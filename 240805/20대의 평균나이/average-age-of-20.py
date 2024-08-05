sum = 0
cnt = 0
while True:
    n = int(input())
    if 20 <= n <= 29:
        sum += n
        cnt += 1
        continue
    else:
        break
print(f"{sum/cnt:.2f}")