#테스트 케이스 T 입력
t = int(input())

#n, m 입력
n, m = map(int, input().split())

#금 개수 입력
array = list(map(int, input().split()))

dp = []
for i in range(0, len(array), m):
	dp.append(array[i:i+m])
    
for j in range(1,m):
	for i in range(n):
        if i == 0: #왼쪽 위에서 오는 경우 
        	left_up = 0
        else: 
        	left_up = dp[i-1][j-1]
        if i == n-1:  #왼쪽아래에서 오는 경우
        	left_down =0 
        else:
        	left_down = dp[i+1][j-1]
        #왼쪽에서 오는 경우
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        
        
result = 0
for i in range(n):
	result = max(result, dp[i][m-1]) #가장 오른쪽 열에 가장 큰 값을 찾아 출력
print(result)
