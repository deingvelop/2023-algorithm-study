import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
connect = [ [] for _ in range(N+1) ]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

def dfs(i, group):
    visited[i] = group

    for near_i in connect[i]:
        if visited[near_i] == 0:
            dfs(near_i, group)

    return True

answer = 0
group = 1
for i in range(1,N+1):
    if visited[i] == 0 and dfs(i, group):
        answer +=1
        group  +=1

print(answer)
# print(visited)
