from collections import deque
import sys

f = sys.stdin.readline

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

distance = [-1] *(n+1)
distance[x] = 0

# BFS 부분
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now]+1
            q.append(i)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if k in distance:
  for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
else:
    print(-1)
