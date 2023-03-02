# 유지비 : 길 유지 비용
# N 개의 집과 M 개의 길

# 마을을 두 개로 분리 

# 크루스칼 알고리즘을 사용후, 
# 가장 비용이 큰 길을 삭제

import sys
input = sys.stdin.readline


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [ i for i in range(N+1) ]
roads = []

for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))

roads.sort() # 비용 순으로 정렬
max_road_cost = 0
result = 0

for r in roads:
    cost, a, b = r 
    if find_parent(parent, a) != find_parent(parent, b):
        # Cycle 이 존재하지 않을 경우
        union_parent(parent, a, b)
        max_road_cost = max(max_road_cost, cost)
        result += cost

# 가장 비용이 비싼 길을 제거한다
result -= max_road_cost

print(result)
