# 1. 완전 탐색
def solution(x, answer):

    if x == 1:
        answers.append(answer)
        return

    if x%5 == 0:
        solution(x//5, answer+1)

    if x%3 == 0:
        solution(x//3, answer+1)

    if x%2 ==0:
        solution(x//2, answer+1)
    
    solution(x-1, answer+1)

answers = []
solution(26, 0)
answers.sort()
print(answers[0])


# 2. DP (보텀업)
x = int(input())

# 계산된 결과 저장
d = [0]*30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2] +1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] +1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] +1)

print(d[x])
