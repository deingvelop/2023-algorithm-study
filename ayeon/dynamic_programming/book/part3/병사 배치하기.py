n = int(input())
s = list(map(int, input().split()))

dp = [1] * n
# 앞쪽에 있는 값이 항상 뒤보다 커야함
# 남아있는 병사 수가 최대가 되어야 함

for i in range(n):
    for j in range(i):
        # 내림차순이면 
        if s[i] < s[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
