import sys
input = sys.stdin.readline

n = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
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


x_list = []
y_list = []
z_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append([x, i])
    y_list.append([y, i])
    z_list.append([z, i])

x_list.sort()
y_list.sort()
z_list.sort()

edges = []
result = 0

for i in range(n-1):
    edges.append([x_list[i+1][0] - x_list[i][0], x_list[i][1], x_list[i+1][1]])
    edges.append([y_list[i+1][0] - y_list[i][0], y_list[i][1], y_list[i+1][1]])
    edges.append([z_list[i+1][0] - z_list[i][0], z_list[i][1], z_list[i+1][1]])

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
