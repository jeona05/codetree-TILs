stat = False
n = int(input())
for i in range(2, n):
    if n % i == 0:
        stat = True

if stat == True:
    print('C')
else:
    print('N')