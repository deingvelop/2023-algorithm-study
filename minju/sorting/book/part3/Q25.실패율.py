def solution(n, stages):
    answer = []
    default = [0]*(n+2)
    
    for i in range(1,n+2):
        cnt = stages.count(i)
        default[i] = cnt
        
    result = []
    for i in range(1, len(default)):
        if sum(default[i:])==0:
            result.append([i,0.0])
        else:
            result.append([i, default[i]/sum(default[i:])])
    
    result.sort()
    result.pop()
    
    result.sort(reverse=True, key=lambda x: (x[1],-x[0]))
    answer = list(map(lambda x: x[0], result))
    
    return answer
