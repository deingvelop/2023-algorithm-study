def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i) #array의 count함수 사용하면 간단
        
        #실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        #리스트에 원소 삽입
        answer.append((i,fail))
        length -= count
    
    answer = sorted(answer, key=lambda x:-x[1])
    
    answer = [i[0] for i in answer] #for문 활용
    
    
    return answer