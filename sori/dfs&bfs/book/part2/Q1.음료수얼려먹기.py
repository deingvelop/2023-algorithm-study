n,m = map(int, input().split())
result = 0
graph = []
for i in range(n):
  graph.append( list(map(int, input().split())) )

def dfs(i,j):
    if i < 0 or i>= n or j < 0 or j >=m:
      return False
    
    if graph[i][j] == 0:
      graph[i][j] = 1
      dfs(i-1,j) #상
      dfs(i+1,j) #하
      dfs(i,j-1) #좌
      dfs(i,j+1) #우
      return True
    return False

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result +=1

print(result)