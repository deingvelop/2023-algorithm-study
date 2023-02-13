#n입력값 받기
n =int(input())

#array 입력값 받기
array = []
for i in range(n) :
  array.append(list(map(int, input().split())))
#dp 테이블 생성
dp = [0]*(n+1)

max_value=0
for i in range(n-1, -1, -1):
	if array[i][0] + i <=n :
    	dp[i] = max(array[i][1] + dp[array[i][0] + i], max_value)
        max_value = dp[i]
    else:
    	dp[i] = max_value
        
print(dp[0])  
