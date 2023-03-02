# 모든 간선을 만들어보지 않고, 선택될 가능성이 있는 간선만 구성해야 한다

import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(x)
    return parent[x]


def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        b = find_parent(a)
    else:
        a = find_parent(b)

# 좌표를 x,y,z 별로 저장하고 정렬
N = int(input())
xlist , ylist, zlist = [], [], []

for i in range(N):
    x,y,z = map(int, input().split())
    xlist.append((x,i))
    ylist.append((y,i))
    zlist.append((z,i))

xlist.sort()
ylist.sort()
zlist.sort()

# 인접한 행성들끼리 간선 구성
edges = []

for curList in xlist, ylist, zlist:
    for i in range(N-1):
        w1, a = curList[i]
        w2, b = curList[i+1]
        
        edges.append((abs(w1-w2), a,b))

edges.sort(reverse=True)

# 크루스칼 진행
parent = [ i for i in range(N+1) ]
count, answer = N-1, 0

while count:
    w, a, b = edges.pop()
    if find_parent(a) == find_parent(b):
        continue
    union_parent(a,b)
    count -= 1
    answer += w1

parent(answer)
