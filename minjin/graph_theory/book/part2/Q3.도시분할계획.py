import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
answer = 0
parent = [0] * (n+1)
max_cost = 0

for i in range(1, n+1):
    parent[i] = i


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])

edges.sort()

# 사이클이 발생하는지 확인
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        answer += cost
        union_parent(parent, a, b)
        max_cost = cost

answer -= max_cost
print(answer)