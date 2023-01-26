N, M = map(int, input().split())
ice = [ list(map(int, input())) for _ in range(N) ]

answer = 0

def ice_cream(x, y, count):
    # 현재 ice[y][x]
    
    ice[y][x] = 3
    count += 1
        
    if y > 0 : # 북
        if ice[y-1][x] == 0:
            ice_cream(x,y-1, count)
    if x > 0 : # 서
        if ice[y][x-1] == 0:
            ice_cream(x-1,y, count)
    if y < N-1 : # 남 
        if ice[y+1][x] == 0:
            ice_cream(x,y+1, count)
    if x < M-1 : # 동
        if ice[y][x+1] == 0:
            ice_cream(x+1,y, count) 
      
    return count 
    # 상 ice[y-1][x]
    # 하 ice[y+1][x]
    # 좌 ice[y][x-1]
    # 우 ice[y][x+1]

# x,y
# ice_cream(0,3,visited, 0)

# for v in ice:
#     print(v)
    
for i in range(N):
    for j in range(M):
        if ice[i][j] == 0:
            if ice_cream(j, i, 0) != 0:
                answer += 1

print(answer)
