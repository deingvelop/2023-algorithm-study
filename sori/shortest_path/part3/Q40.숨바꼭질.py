import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  # a, b 연결: 양방향이기 대문에 둘다 연결해줘야함
  graph[a].append((b,1))
  graph[b].append((a,1))

INF = int(1e9)
start = 1
distance = [INF] * (n+1)

def dijkstra(start):
  #시작 노드
  distance[start] = 0
  q = []
  heapq.heappush(q, (0,start))
  while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
      continue
    for idx, dis in graph[node]:
      cost = distance[node] + dis
      if cost < distance[idx]:
        distance[idx] = cost
        heapq.heappush(q,(cost, idx))

  #1번부터 가장 먼 헛간까지의 거리 구하기
  max_dist = -1
  for i in range(1, n+1):
    if distance[i] != INF:
      max_dist = max(max_dist, distance[i])
      
  #거리가 같은 노드중 가장 작은 헛간 번호랑 갯수
  node = []
  for i in range(1, n+1):
    if distance[i] == max_dist:
      node.append(i)
  print(node[0], max_dist, len(node))