# O(N^3) 해결 방법 : 설치 및 삭제 연산을 요구할 때마다 일일이 <전체 구조물을 확인> 하는 것
# 가능한지 확인 후 -> 적용 보다, <우선 적용> 이후 <확인> 이후 부가적으로 <삭제/추가> 연산 이어서 하기

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            # '바닥 위' / '보의 한쪽 끝부분 위' / '다른 기둥 위' -> 정상
            if y == 0 or
            [x-1, y, 1] in answer  or [x, y, 1] in answer or 
            [x, y-1, 0] in answer :
                continue
            return False

        elif stuff == 1: # 보
            # 한쪽 끝부분이 기둥 위 / 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] or
                ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame

        if operate == 0: # 삭제
            answer.remove([x,y,stuff]) # 일단 삭제
            if not possible(answer): # 이후에 가능한지 확인
                answer.append([x,y,stuff]) # 아니면 다시 설치

        
        if operate == 1 : # 설치
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer):
                answer.remove([x,y,stuff])
    
    return sorted(answer)
