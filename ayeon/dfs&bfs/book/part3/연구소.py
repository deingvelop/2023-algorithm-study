from itertools import combinations
import copy 

N, M = map(int, input().split())

lab = [ list(map(int, input().split())) for _ in range(N) ]
#  (3 ≤ N, M ≤ 8)

empty = [] # 빈칸 좌표 lab[i][j]
virus = [] 

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0: # 빈칸
            empty.append([i, j])
        elif lab[i][j] == 2: # 바이러스
            virus.append([i, j])


walls = list(combinations(empty,3)) # 벽 3개를 뽑아보자

def spread(i, j, lab):
    # 현재 lab[i][j]
    # print(i,j)
    lab[i][j] = 2
    
    # for l in lab:
    #     print(l)
    if i > 0 and lab[i-1][j] == 0:
        # 북
        spread(i-1, j, lab)
    if j > 0 and lab[i][j-1] == 0:
        # 서
        spread(i, j-1, lab)
    if i < N-1 and lab[i+1][j] == 0:
        # 남
        spread(i+1, j, lab)
    if j < M-1 and lab[i][j+1] == 0:
        # 동
        spread(i, j+1, lab)

    return True


def safe_zone(lab):
    answer = 0

    # 바이러스들 시작
    for vir in virus:
        # 증식하기
        spread(vir[0], vir[1], lab)
    
    # 안전 영역 개수 세기
    for la in lab:
        for l in la:
            if l == 0:
                answer +=1

    return answer


answer = 0
for wall in walls:

    lab2 = copy.deepcopy(lab)   # 새로운 실험실 깊은 복사
    
    for w in wall: # 벽 설치
        lab2[w[0]][w[1]] = 3
    
    answer = max(answer, safe_zone(lab2)) # 안전 영역 크기 계산 후 갱신

print(answer)
