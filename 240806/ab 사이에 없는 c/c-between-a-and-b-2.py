stat = True
arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
for i in range(a, b+1):
    if i % c == 0:
        stat = False
if stat == False:
    print('NO')
else:
    print('YES')