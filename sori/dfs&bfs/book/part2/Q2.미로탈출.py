from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = dx[i]+x
      ny = dy[i]+y
  
      if nx < 0 or nx >= n or ny < 0 or ny >=m:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  
  return graph[n-1][m-1]

print(bfs(0,0))

#가까운 노드 탐색 -> bfs
#bfs는 큐 자료구조 사용 잊지말기!