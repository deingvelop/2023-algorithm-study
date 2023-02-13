N = int(input())
T = []
P = []

# 입력
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 풀이
d = [0] * (N+2) # i 번째날까지 일을 했을 때, 최댓값.

for i in range(N-1, -1, -1):
    if T[i]+i <= N:
        d[i] = max(d[T[i]+i] + P[i], d[i+1])
        # i번째 날 일을 하면, (T[i] + i)날 일을 한 돈 + 지금 버는 돈 vs 다음날 (i+1) 의 돈
        # i번째 날, 일을 안하면, i+1 번째 날 일한 거랑 동일
    else:
        d[i] = d[i+1]

print(d[0])
