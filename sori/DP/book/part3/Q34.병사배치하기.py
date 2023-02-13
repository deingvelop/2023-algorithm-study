#DP 중 유명한 알고리즘인 '가장 긴 증가하는 부분수열 문제'

n = int(input())
soldiers = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분수열' 문제로 변환
soldiers.reverse()

# 1차원 DP테이블 초기화
dp = [1] * n 
for i in range(1, n):
    for j in range(0, i): # 처음부터 i까지 끝까지 비교한다.
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1) #현재 i까지 입력된 최대값을 그냥 쓸건지 아니면 다른 흐름에 탑승할 것인지 결저
print(n-max(dp))