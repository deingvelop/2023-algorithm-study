N, M = map(int, input().split())
x0, y0, r0 = map(int, input().split())


place = []
for i in range(N):
    place.append(list(map(int, input().split())))

# 메뉴얼에 따라 이동, 캐릭터가 방문한 칸의 수를 출력
answer = 0

# r0  = 0 : 북, 1 : 동, 2 : 남, 3 : 서

# place[i][j] = 0: 육지, 1: 바다

rotations = [
    (-1, 0), # N
    (0, 1), # E
    (1, 0), # S
    (0, -1) # W
    ] 


def left(r):
    # r == 0 -> 3 
    # r == 1 -> 0
    # r == 2 -> 1
    # r == 3 -> 2
    if r==0: return 3
    return r-1
    

def back_sea(x, y, r):
    if place[y-r][x-r] == 1:
        return True
    return False


def back(x, y, r):
    return x-r, y-r

x, y, r = x0, y0, r0

if place[y][x] == 0:
    place[y][x] = 2
    answer += 1

while True:
    flag = False

    # 1) 현재 방향을 기준으로 왼쪽 방향
    for i in range(4): 
        nr = left(r)

        dx = rotations[nr][0]
        dy = rotations[nr][1]
        
        # 2) 가보지 않은 칸 존재
        if ( place[y+dy][x+dx] == 0 ):
            # 회전
            r = nr

            # 전진
            x += dx
            y += dy

            answer += 1
            place[y][x] = 2 # 방문한 자리는 2
            flag = True

            break

        else:
            # 회전
            r = nr
    
    # 3) 네 방향 -> 이미 가본 칸 or 바다로 되어 있는 칸 :
    if flag == False: 
        
        # 뒤쪽 방향이 바다이면 멈춘다
        if back_sea(x,y,r) == True:
            break;

        # 방향 유지, 뒤로 한칸
        x, y = back(x, y, r)
    
print(answer)
