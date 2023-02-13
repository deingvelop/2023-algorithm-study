import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coin = [ int(input()) for _ in range(n) ]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001]*(m+1)

# DP
d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        d[j] = min(d[j], d[j-coin[i]]+1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
