# # 나의 풀이 - 테스트케이스 12번만 오류
# def solution(N, stages):
#     failures = [0 for _ in range(N+1)]
#     reaches = [0 for _ in range(N + 1)]
#     fail_rates = [[i, 0] for i in range(N+1)]
#
#     for stage in stages:
#         if stage == N+1:
#             reaches[N] += 1
#             for s in range(1, stage):
#                 reaches[s] += 1
#         else:
#             failures[stage] += 1
#             for s in range(1, stage+1):
#                 reaches[s] += 1
#
#     for i in range(1, N+1):
#         if reaches[i] == 0:
#             fail_rates[i][1] = 0
#         else:
#             fail_rates[i][1] = failures[i] / reaches[i]
#     del fail_rates[0]
#     fail_rates.sort(key=lambda x:(-x[1], x[0]))
#
#     answer = []
#     for f in fail_rates:
#         # if f[0] != 0:
#             answer.append(f[0])
#     return answer
#
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(10, [1, 2, 3, 3, 4, 5, 5]))
# print(solution(5,[2, 2, 2, 2, 2, 2, 2, 2]))
# print(solution(1,[1]))
# print(solution(1,[2]))


# # 교재 풀이
# def solution(N, stages):
#     answer = []
#     length = len(stages)
#
#     for i in range(1, N+1):
#         count = stages.count(i)
#
#         if length == 0:
#             fail = 0
#         else:
#             fail = count / length
#
#         answer.append((i, fail))
#         length -= count
#
#     answer = sorted(answer, key=lambda x:-x[1])
#     answer = [i[0] for i in answer]
#     return answer


# 스터디 후 코드 수정
def solution(N, stages):
    fail_rates = [[i, 0] for i in range(N+1)]
    users_in_stages = [stages.count(i) for i in range(N+2)]

    for i in range(1, N+1):
        if users_in_stages[i] == 0:
            fail_rates[i][1] = 0
        else:
            fail_rates[i][1] = users_in_stages[i] / sum(users_in_stages[i:])
    del fail_rates[0]

    fail_rates.sort(key=lambda x:(-x[1], x[0]))
    fail_rates = [f[0] for f in fail_rates]
    return fail_rates

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))