n = int(input())  #보드의 크기
k = int(input())  #사과의 개수

data = [[0]*n for i in range(n)]  #초기배열 

for _ in range(k):
  x, y = map(int, input().split())
  data[x][y] = 1 #사과 있는 곳 표시
  
l = int(input())  #방향 변환 횟수 
info = [] #방향회전정보 

for _ in range(l):
  x, c = input().split()
  info.append((int(x),c))

#처음에는 오른쪽으로 보고있으므로 동-남-서-북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  

def turn(direction,c):
  if c == 'L' :
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4
  
  return direction

def simulate():
  x,y = 1, 1 #뱀의 머리 위치
  data[x][y] =2 #뱀이 존재하는 위치는 2로 표시

  direction = 0 #처음에는 동쪽을 보고 있음
  time = 0 #시작한 뒤에 지난 '초' 시간
  index = 0 #다음에 회전할 정보

  q = [(x,y)]
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

  #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면 
    if 1 <= nx and nx <=n and 1 <= ny and ny<=n and data[nx][ny] != 2:
    #사과가 이동이 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0 :
        data[nx][ny] = 2
        q.append((nx,ny))
        px,py = q.pop(0)
        data[px][py] = 0
    #사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] ==1:
        data[nx][ny] = 2
        q.append((nx,ny))

  #벽이나 뱀의 몸통과 부딪혔다면 
    else:
      time = time +1 
      break

  x,y = nx,ny
  time = time +1
  if index < 1 and time == info[index][0]:
    direction = turn(direction, info[index][1])
    index += 1
  return time
