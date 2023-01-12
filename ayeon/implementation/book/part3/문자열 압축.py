def solution(s):
    answer = len(s)
    
    for i in range(1,len(s)//2+1):
        s2 = ""
        sliced = []
    
        for j in range(0, len(s), i):
            sliced.append(s[j:j+i])

        s0 = sliced[0]
        count = 1
        for j in range(1, len(sliced)):
            if s0 == sliced[j]:
                count +=1
            else:
                if count != 1:
                    s2 += str(count)
                s2 += s0

                # update
                s0 = sliced[j]
                count = 1

        if count != 1:
            s2 += str(count)
        s2 += s0

        if answer > len(s2):
            answer = len(s2)
        
    return answer
