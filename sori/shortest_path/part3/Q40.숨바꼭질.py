import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  # a, b 연결: 양방향이기 대문에 둘다 연결해줘야함
  graph[a].append((b,1))
  graph[b].append((a,1))

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
  #시작 노드
  distance[start] = 0
  q = []
  #시작 노드로 가는 최단경로는 0으로 설정
  heapq.heappush(q, (0,start))
  while q:
    dist, node = heapq.heappop(q)
    #이미 처리되어 있으면 무시
    if dist > distance[node]:
      continue
    #현재 노드와 연결된 다른 인접 노드들을 확인
    for idx, dis in graph[node]:
      cost = distance[node] + dis
      #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 업데이트하기
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
      #숨어야하는 헛간번호(가장번호작은), 거리, 같은 거리 헛간갯수
  print(node[0], max_dist, len(node))

dijkstra(1)