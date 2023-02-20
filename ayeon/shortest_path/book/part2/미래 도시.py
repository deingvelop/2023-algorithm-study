N, M = map(int, input().split())
path = [[] for _ in range(M+1)]

INF = int(1e9)
for i in range(M):
    f1, f2 = map(int, input().split())
    path[f1].append(f2)
    path[f2].append(f1)

X, K = map(int, input().split())

distance1 = [INF]*(N+1) # 1번 회사 -> K번 회사
distance2 = [INF]*(N+1) # K번 회사 -> x번 회사

visited1 = [False]*(N+1)
visited2 = [False]*(N+1)


def get_smallest_node(distance, visited):
    min_value = INF
    index = 0

    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index


def dijkstra(start, distance, visited):

    distance[start] = 0
    visited[start] = True

    for i in path[start]:
        distance[i] = 1
    
    for i in range(N-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node(distance, visited)
        visited[now] = True
        
        for j in path[now]:
            print(path[now])
            distance[j] = min(distance[j], distance[now]+1)

dijkstra(1, distance1, visited1)
dijkstra(K, distance2, visited2)

print(distance1[K]+distance2[X])
