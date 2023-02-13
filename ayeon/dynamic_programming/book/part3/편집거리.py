str1 = input()
str2 = input()

# dp 
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1, len(str1)+1):
    dp[0][i] = i

for i in range(1, len(str2)+1):
    dp[i][0] = i

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):

        # 문자가 다른 경우
        if str1[j-1] != str2[i-1]:
            # 위(삭제), 왼쪽 위(교체), 왼(삽입)
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1

        # 문자가 같은 경우
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[len(str2)][len(str1)])
