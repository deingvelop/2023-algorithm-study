#내가 푼 풀이 -> 시간초과
from collections import deque

def bfs(graph, x, distance):
  queue = deque([x])
  idx = 0
  while queue:
    v = queue.popleft()
    idx+=1
    for i in graph:
      a,b = i[0],i[1]
      if v == a:
        if distance[b] == 0:
          queue.append(b)
          distance[b] += idx
          if distance[b] == k:
            result.append(b)

  return result

n, m, k, x = map(int, input().split())
graph = []
result = []
distance = [0]*(n+1)
for i in range(m):
   a, b = map(int, input().split())
   graph.append((a,b))

result = bfs(graph, x ,distance)

if len(result) == 0:
  print(-1)
else:
  for i in result:
    print(i)
  

#고친 풀이
from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)