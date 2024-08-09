n = int(input())
for i in range(n):
    for j in range(i):
        print("  ", end="") #어이없는 부분: 공백이 두칸이어야되;; 공백한칸은 n=3일때 두번째 줄 공백이 한칸 덜 생기면서 균열 시작

    for j in range(2 * n - 2 * i - 1): #이것또한이해못함(힌트보고그대로적은거임)
        print("*", end=" ")
    print()