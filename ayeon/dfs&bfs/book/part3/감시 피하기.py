from itertools import combinations

N = int(input())
hall = [ list(input().split()) for _ in range(N) ]

teachers = []
emptys = []           
for i in range(N):
    for j in range(N):
        if hall[i][j] == 'T':
            teachers.append([i,j])
        if hall[i][j] == 'X':
            emptys.append([i,j])
                 
def check(hall):
    # (i, j) 에 "장애물"이 있을 때
    # 학생들이 감시를 모두 피할 수 있으면 True
    # else return False
    for teacher in teachers:
        tx, ty = teacher[0], teacher[1]
        
        # 상
        flag_u = 'X'
        for i in range(1,N):
            if tx-i < 0:
                break
            
            if flag_u == 'X' and hall[tx-i][ty] == 'O':
                flag_u = 'O'
                break
            
            if hall[tx-i][ty] == 'S':
                flag_u = 'S'
                break
        
        if flag_u == 'S':
            return False

        # 하
        flag_d = 'X'
        for i in range(1,N):
            if tx+i > N-1:
                break
            
            if flag_d == 'X' and hall[tx+i][ty] == 'O':
                flag_d = 'O'
                break
            
            if hall[tx+i][ty] == 'S':
                flag_d = 'S'
                break
                
        if flag_d == 'S':
            return False

        # 좌
        flag_l = 'X'
        for i in range(1,N):
            if ty-i < 0:
                break
            
            if flag_l == 'X' and hall[tx][ty-i] == 'O':
                flag_l = 'O'
                break
            
            if hall[tx][ty-i] == 'S':
                flag_l = 'S'
                break
        
        if flag_l == 'S':
            return False

        # 우
        flag_r = 'X'
        for i in range(1,N):
            if ty+i > N-1:
                break
            
            if flag_r == 'X' and hall[tx][ty+i] == 'O':
                flag_r = 'O'
                break
            
            if hall[tx][ty+i] == 'S':
                flag_r = 'S'
                break

        if flag_r == 'S':
            return False

    return True


possible_o = combinations(emptys, 3)

flag = False
for obstacles in possible_o:
    for o in obstacles:
        hall[o[0]][o[1]] = 'O'
    
    if check(hall):
        flag = True
        # for h in hall:
        #     print(h)
        break
    
    for o in obstacles:
        hall[o[0]][o[1]] = 'X' # 되돌리기

if flag:
    print("YES")
else:
    print("NO")
