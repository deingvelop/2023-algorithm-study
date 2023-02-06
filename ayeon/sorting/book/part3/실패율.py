def solution(N, stages):
    answer = []

    users_in_stages = [0]*(N+2)
    fails = [ [i,0] for i in range(N+1) ]
    
    for s in stages:
        users_in_stages[s] +=1

    for i in range(1,N+1):
        if users_in_stages[i] == 0:
            fails[i][1] = 0
        else:
            fails[i][1] =  users_in_stages[i] / sum(users_in_stages[i:])
    
    fails.remove([0,0])
    fails.sort(key= lambda x:(-x[1], x[0]))
    
    for f in fails:
        answer.append(f[0])
              
    return answer
