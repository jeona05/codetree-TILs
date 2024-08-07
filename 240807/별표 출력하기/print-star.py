n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print()

for k in range(n-1):
    for j in range(n-1-k):
        print('*', end=" ")
    print()