import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = 0

i = len(coins) - 1
while k > 0 and i >= 0:
    cnt = k // coins[i]
    answer += cnt
    k -= coins[i] * cnt
    i -= 1

print(answer)