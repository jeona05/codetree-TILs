stat = True
n = int(input())
for i in range(2, n):
    if n % i == 0:
        stat = False
if stat == True:
    print('P')
else:
    print('C')