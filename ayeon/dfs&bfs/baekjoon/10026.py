# 크기가 N×N 그리드
# R(빨강), G(초록), B(파랑)
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수

import sys
sys.setrecursionlimit(10**6)

N = int(input())
paint1 = []

for i in range(N):
    paint1.append(list(input()))
    # 'R', 'G', 'B'

paint2 = [ arr[:] for arr in paint1 ] # 깊은 복사

answer1 = 0
answer2 = 0

def dfs(i, j, paint, color):
    
    if i<0 or i>N-1 or j<0 or j>N-1:
        return False

    if color != paint[i][j]:
        return False
    
    # 같은 색상이면, 표시
    paint[i][j] = 'X'

    dfs(i+1, j, paint, color)
    dfs(i-1, j, paint, color)
    dfs(i, j+1, paint, color)    
    dfs(i, j-1, paint, color)
    
    return True

def dfs2(i, j, paint, color):

    if i<0 or i>N-1 or j<0 or j>N-1:
        return False

    this_color = paint[i][j]
    
    if (color == 'R' and this_color == 'G') or (color == 'G' and this_color == 'R') or (color == this_color) :

        # 같은 색상이면, 표시
        paint[i][j] = 'X'
        
        dfs2(i+1, j, paint, color) # dfs , dfs2 구분!
        dfs2(i-1, j, paint, color)
        dfs2(i, j+1, paint, color)    
        dfs2(i, j-1, paint, color)
        return True
    
    return False

for i in range(N):
    for j in range(N):
        if paint1[i][j] != 'X':
            if dfs(i, j, paint1, paint1[i][j]):
                answer1 += 1

for i in range(N):
    for j in range(N):
        if paint2[i][j] != 'X':
            if dfs2(i, j, paint2, paint2[i][j]):
                answer2 += 1

print(answer1, answer2)
