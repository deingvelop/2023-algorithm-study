import heapq

for _ in range(int(input())):
  n = int(input())
  INF = int(1e9)
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  distance = [[INF]* n for _ in range(n)]

  dx = [0,0,1,-1]
  dy = [1,-1,0,0]

  q = []
  heapq.heappush(q, (graph[0][0], 0, 0)) # cost, x, y
  distance[0][0] = graph[0][0]
  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for i in range(4):
      nx, ny = x + dx[i], y+dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q,(cost, nx, ny))

  print(distance[n-1][n-1])