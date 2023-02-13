n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * 10001

for coin in coins:
    dp[coin] = 1

for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[m] == 1001:
    print(-1)
else:
    print(dp[m])