arr = input().split()
a, b = int(arr[0]), int(arr[1])
for i in range(1, 10):
    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {i*j} ", end="")
        if a != b and j > a:
            print("/", end=" ")
    print()
'''
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} * {j} = {i*j}", end="")
        if j < n:
            print("/", end=" ")
    print()
'''