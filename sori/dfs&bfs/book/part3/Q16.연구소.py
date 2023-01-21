#내 풀이
from itertools import combinations
import sys
f = sys.stdin.readline

n,m = map(int, f().split())
graph = []
visited = [[False] *n for _ in range(m)]
lst_zero = []
result = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(graph, i,j):
  if graph[i][j] == 0:
    graph[i][j] = 2
    #visited[i][j] = True
    for z in range(4):
         nx = dx[z]+i
         ny = dy[z]+j
         if 0<= nx <n and 0<= ny <m: 
              
             #if visited[nx][ny] == False:
               dfs(graph, nx,ny)
  

for i in range(n):
  graph.append( list(map(int, f().split())))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      lst_zero.append((i,j))

lst_cmb = list(combinations(lst_zero,3))


for i in lst_cmb:
  graph_2 = graph
  for x,y in i:
    graph_2[x][y] = 1

  for i in range(n):
    for j in range(m):
       if graph_2[i][j] == 2:
         dfs(graph_2, i,j)
  cnt = 0      
  for i in range(n):
    for j in range(m):
       if graph_2[i][j] == 0:
         cnt += 1
  #print(graph)
  result = max(result, cnt)

print(result)

#고친 풀이