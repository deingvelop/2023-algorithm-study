import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
conn = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    conn[a][b] = min(conn[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            conn[i][j] = 0

def floyd():
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                conn[a][b] = min(conn[a][b], conn[a][k] + conn[k][b])


floyd()


for x in range(1, n+1):
    for y in range(1, n+1):
        if conn[x][y] == INF:
            conn[x][y] = 0
    answer = conn[x][1:]
    print(*answer)