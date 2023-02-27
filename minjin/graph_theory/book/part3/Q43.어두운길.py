import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append([cost, x, y])

edges.sort()

total_cost = 0
min_cost = 0
# 사이클 일어나는지 확인
for edge in edges:
    cost, a, b = edge
    total_cost += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost

print(total_cost - min_cost)