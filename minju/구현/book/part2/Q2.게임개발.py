n, m = map(int, input().split())
a, b, d = map(int, input().split()) #현재 위치

array = []
for i in range(n):
  array.append(list(map(int, input().split())))
 
map = [[0]*m for i in range(n)]
map[a][b] = 1 #현재 위치 

#반시계방향 이니까 북-동-남-서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1 
turn_time = 0

while True:
  d = d -1 #북:0, 동:1, 남:2, 서:3
  if d<0:
    d = 3
  
  nx = a + dx[d]
  ny = b + dy[d]

  if array[nx][ny] == 0:
    array[nx][ny] = 1
    a,b = nx, ny
    count = count + 1
    turn_time = 0
  else:
    turn_time = turn_time + 1
  
  if turn_time == 4:
    nx = a - dx[d]
    ny = b - dy[d]

    if array[nx][ny] == 0:
      a, b = nx, ny 
    else:
      break
    trun_time = 0

print(count)
