# 내 풀이
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

left, right = 1, houses[n-1] - houses[0]
answer = 0

if c == 2:
    print(houses[n-1] - houses[0])

else:
    while left < right:
        mid = (left + right) // 2

        cnt = 1
        last_built = houses[0]

        for i in range(n):
            if houses[i] - last_built >= mid:
                cnt += 1
                last_built = houses[i]

        if cnt >= c:
            answer = mid
            left = mid + 1
        elif cnt < c:
            right = mid

    print(answer)


# # 정답 풀이
# import sys
# input = sys.stdin.readline
#
# n, c = map(int, input().split())
# h = [int(input()) for i in range(n)]
# h.sort()
#
# start, end = 1, h[n-1] - h[0]
# # 집 사이의 최소 거리, 최대 거리
# result = 0
#
# if c == 2:
#     print(h[n-1] - h[0])
#     # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
# else:
#     while start < end:
#         mid = (start + end)//2
#
#         count = 1
#         ts = h[0]
#         # 마지막으로 설치된 공유기의 위치
#         for i in range(n):
#             if h[i] - ts >= mid:
#                 count += 1
#                 ts = h[i]
#         if count >= c:
#             result = mid
#             start = mid + 1
#         elif count < c:
#             end = mid
#     print(result)