import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
conn = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    low, high = map(int, input().split())
    conn[low][high] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            conn[i][j] = 0

def floyd():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                conn[a][b] = min(conn[a][b], conn[a][k] + conn[k][b])


floyd()


answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if conn[i][j] != INF or conn[j][i] != INF:
            cnt += 1
    if cnt == n:
        answer += 1

print(answer)