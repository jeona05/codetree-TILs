n = int(input())
for i in range(n): #n+1로 했을 땐 출력 시 공백이 한 줄 더 나옴...왜
    for j in range(2*i+1): #2*i-1
        print('*', end="")
    print()