import sys

input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    name, k, e, m = input().split()
    k = int(k)
    e = int(e)
    m = int(m)

    arr.append([name, k, e, m])

# 1. 국어 점수가 감소하는 순서
# 2. 영어 점수가 증가하는 순서
# 3. 수학 점수가 감소하는 순서
# 4. 이름이 사전 순으로 증가하는 순서
arr.sort(key= lambda x:(-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])
