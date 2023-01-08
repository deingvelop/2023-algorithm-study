# 풀이 1 - itertools 활용 (greedy x)
import itertools

n, m = map(int, input().split())
balls = list(map(int, input().split()))

combs = itertools.combinations(balls, 2)
answer_list = list(filter(lambda c: len(set(c)) > 1, combs))
print(len(answer_list))


# 풀이 2 - greedy
n, m = map(int, input().split())
balls = list(map(int, input().split()))

ball_cnt = [0 for _ in range(n+1)]
for i in range(len(ball_cnt)):
    ball_cnt[i] = balls.count(i)

answer = 0
for num in range(n):
    answer += ball_cnt[num] * (sum(ball_cnt) - ball_cnt[num])

print(answer // 2)


# 풀이 3 - greedy (교재)
n, m = map(int, input().split())
balls = list(map(int, input().split()))

ball_cnt = [0 for _ in range(n+1)]
for ball in balls:
    ball_cnt[ball] += 1

answer = 0
for i in range(1, m+1):
    n -= ball_cnt[i]
    answer += ball_cnt[i] * n

print(answer)