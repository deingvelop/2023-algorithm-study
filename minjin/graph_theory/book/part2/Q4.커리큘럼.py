import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)
answer = [0] * (n+1)

for e in range(1, n+1):
    edge_info = list(map(int, input().split()))
    times[e] = edge_info[0]
    for conn_e in edge_info[1:-1]:
        graph[conn_e].append(e)
        indegree[e] += 1

q = deque([])
for e in range(1, n+1):
    if indegree[e] == 0:
        q.append(e)

while q:
    now_e = q.popleft()
    answer[now_e] += times[now_e]
    for conn_e in graph[now_e]:
        answer[conn_e] += times[now_e]
        indegree[conn_e] -= 1
        if indegree[conn_e] == 0:
            q.append(conn_e)

for a in answer[1:]:
    print(a)