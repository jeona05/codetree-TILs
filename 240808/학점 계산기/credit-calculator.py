n = int(input())
arr = list(map(float, input().split())) # 여기 처음에 int로 썼다가 출력 평균 학점에서 틀림;
print(f"{sum(arr)/len(arr):.1f}")
if sum(arr)/len(arr) >= 4.0:
    print("Perfect")
elif sum(arr)/len(arr) >= 3.0:
    print("Good")
else:
    print("Poor")