N = int(input())
number = list(map(int, input().split())) # N 개
opr = list(map(int, input().split())) # N-1 개

operator = []
for i in range(opr[0]):
    operator.add(1)     # + 갯수
for i in range(opr[1]):
    operator.add(2)     # - 갯수
for i in range(opr[2]):
    operator.add(3)     # x 갯수
for i in range(opr[3]):
    operator.add(4)     # % 갯수

max_result = -1000000000
min_result = 1000000000

from itertools import permutations

po = permutations(operator,len(operator))
# list(set(list(itertools.permutations(opr2, N-1)))) 중복 제거
for o in po:

    answer = number[0]
    for i in range(1,N):

        o1 = operator[i] 
        if o1 == 1:
            answer += number[i]
        elif o1 == 2:
            answer -= number[i]
        elif o1 == 3:
            answer *= number[i]
        else:
            if answer<0:
                answer  = (answer*(-1) //number[i]) *(-1)
            else:
                answer //= number[i]
    
    max_result = max(max_result, answer)
    min_result = min(min_result, answer)

print(max_result)
print(min_result)
