# N개의 집, M 개의 도로
# 집 : 0 ~ N-1
# 도로 가로등 비용 : 도로의 길이

# 가로등이 켜진 도로만 사용 가능
# 일부 가로등을 절약할 수 있는 최대 금액

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

costs = []

resut = 0

for _ in range(M):
    x, y, z = map(int, input().split())

    costs.append((z, x, y))

costs.sort()

parent = [ i for i in range(N) ]


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

result = 0

for cost in costs:
    c, x, y = cost
    
    if find_parent(parent, x) == find_parent(parent, y):
        # 절약
        result += c
    else:
        # 가로등 도로 사용
        union_parent(parent, x, y)

print(result)
