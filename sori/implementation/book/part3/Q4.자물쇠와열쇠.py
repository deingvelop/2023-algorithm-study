  def create_graph(n, lock):
      graph = [[0] * (n*3) for _ in range(n * 3)]
      for i in range(n):
          for j in range(n):
              graph[i + n][j + n] = lock[i][j]
      return graph
 
 
  def unlock(n, graph):
      for i in range(n, n * 2):
          for j in range(n, n * 2):
              if graph[i][j] != 1:
                  return False
      return True
 
 
  def rotate(m, key):
      nkey = [[0] * m for _ in range(m)]
      for i in range(m):
          for j in range(m):
              nkey[j][-i + m - 1] = key[i][j]
      return nkey
 
 
  def solution(key, lock):
      n, m = len(lock), len(key)
      graph = create_graph(n, lock)
 
      for _ in range(4):  # 90, 180, 270, 360
          key = rotate(m, key)
          for x in range(n * 2):
              for y in range(n * 2):
 
                  for i in range(m):
                      for j in range(m):
                          graph[x + i][y + j] += key[i][j]
 
                  if unlock(n, graph):
                      return True
 
                  for i in range(m):
                      for j in range(m):
                          graph[x + i][y + j] -= key[i][j]
 
      return False

#구현, 완전탐색 인터넷 풀이 참고