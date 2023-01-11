n, m = map(int, input().split()) # 맵 크기
a, b, d = map(int, input().split()) # 캐릭터 좌표/ 방향

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 0:육지, 1:바다, 2:가본칸
result = 1
map_data = []
for i in range(n):
  map_data.insert(i,list(map(int, input().split())))

count = 0
while True:
  
  if(d == 0):
    d = 3
  else :
    d -= 1
    
  na = a + dx[d]
  nb = b + dy[d]
  if(map_data[na][nb] == 0):
      result += 1
      map_data[na][nb] = 2
      a = na
      b = nb
      count = 0
      continue
  else : 
      count+= 1
      
  if(count == 4):
      na = a - dx[d]
      nb = b + dy[d]
      if(map_data[na][nb] == 2):
        a = na
        b = nb
      else : 
        break
      count = 0
print(result)