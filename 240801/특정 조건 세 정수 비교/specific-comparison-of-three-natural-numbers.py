arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
min = 0

if a <= b and a <= c:
    min = a
    print(1, end=" ")
elif b <= c and b <= a:
    min = b
    print(0, end=" ")
else:
    min = c
    print(0, end=" ")

if a == b and b == c:
    print(1)
else:
    print(0)