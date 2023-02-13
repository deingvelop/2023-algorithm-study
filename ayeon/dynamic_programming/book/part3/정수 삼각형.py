def solution(triangle):
    answer = 0
    
    h = len(triangle)
    
    d = [ [0]*(i+2) for i in range(h)]
    
    for i in range(h):
        for j in range(i+1):
            if j-1 >=0 :
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            d[i][j] = max(d[i][j], d[i-1][j]+triangle[i][j])
        
    answer = max(d[h-1])
        
    return answer
