import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

pq = []
heapq.heappush(pq, (0, 1))
distance[1] = 0

while pq:
    so_far, now = heapq.heappop(pq)
    for connected in graph[now]:
        new_d = so_far + 1
        if distance[connected] < new_d:
            continue
        heapq.heappush(pq, (new_d, connected))
        distance[connected] = min(new_d, distance[connected])


max_d = max(distance[1:])
max_d_node = distance.index(max_d)
max_d_cnt = distance.count(max_d)
print(max_d_node, max_d, max_d_cnt)