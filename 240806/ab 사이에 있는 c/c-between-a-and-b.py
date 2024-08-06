con = False
arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
for i in range(a, b+1):
    if i % c == 0:
        con = True
#    else:
#        break
if con == True:
    print('YES')
else:
    print('NO')