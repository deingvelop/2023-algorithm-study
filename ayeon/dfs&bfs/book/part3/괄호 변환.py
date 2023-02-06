# 올바른 괄호 문자열 확인
def right_string(p): 
    s = []
    i=0
    while i<len(p):
        if len(s) == 0:
            if p[i] == ')':
                return False
            s.append(p[i])
        else:
            if s[-1] == p[i]:
                s.append(p[i])
            else:
                if len(s) < 1:
                    return False
                s.pop()
        i+=1    
    if len(s) != 0:
        return False
    return True

def func_1(p):
    print("p:",p)
    if p == '':
        return p

    cnt_open = 0
    cnt_close = 0

    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            cnt_open +=1
        else:
            cnt_close +=1
        
        if cnt_open > 0 and cnt_open == cnt_close:
            u = p[:i+1]
            v = p[i+1:]
            print(i)
            break

    print("u", u, "v",v)
    if right_string(u): # 3)   
        print("r u", u, "v",v)
        u += func_1(v)
        return u

    else:
        print("nr u", u, "v",v)
        s = '(' # 4-1
        s += func_1(v)
        s += ')'
        print("s",s)
        list1 = list(u[1:len(u)-1])
        for i in range(len(list1)):
            if list1[i] == ')':
                list1[i] = '('
            else:
                list1[i] = ')'
        print(s)
        s += ''.join(list1)
        print(s)
        return s


# p 는 균형잡힌 괄호 문자열
def solution(p):
    answer = ''
    if right_string(p):
        return p
    answer = func_1(p)
    return answer
