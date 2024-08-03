n = int(input())
a = b = c = 0
for i in range(0, n, 2):
    if i % 6 != 0 or i % 12 != 0:
        a += 1
for j in range(0, n, 3):
    if i % 12 != 0:
        b += 1
for k in range(0, n, 12):
    c += 1
print(a-1, b-1, c-1)