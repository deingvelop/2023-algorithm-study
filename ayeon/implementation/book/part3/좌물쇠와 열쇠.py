# 완전 탐색을 수월하게 하기 위해서 좌물쇠 리스트의 크기를 <3배 이상> 으로 변경하면 계산이 수월해진다.

'''
- 2차원 배열 슬라이싱

def slicing(N, idx):
    new_keys = []
    for i in range(N-idx+1):
        for j in range(N-idx+1):
            new = []
            for row in arr[ i : i+n ]:

                new.append( row[j:j+m] )
            news.append(new)
    return new_keys
'''


'''
- 2차원 리스트 왼쪽 방향을 90도 회전
for i in range(4):
    new_key = list(zip(*new_key[::-1]))
'''

# 2차원 리스트 90도 회전
def rotate(arr):
    n = len(arr)
    m = len(arr[0])

    arr2 = [ [0]*n for _ in range(m) ] # 결과 리스트

    for i in range(n):
        for j in range(m):
            arr2[j][n-i-1] = arr[i][j] 
    
    return arr2


# 좌물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 좌물쇠의 크기를 기존의 3배로 변환
    new_lock = [ [0]*(n*3) for _ in range(n*3) ]

    # 새로운 좌물쇠의 중앙 부분에 기존의 좌물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate(key) # 열쇠 회전
        
        for x in range(n*2):
            for y in range(n*2):

                # 좌물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):

                        new_lock[x+i][y+j] += key[i][j]
                    
                # 새로운 좌물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True

                # 좌물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False 
