#퇴사 최대수익
#뒤에서 부터 접근해서 수익을 더해감
#현재 인덱스의 걸리는 시간 + 현재 날짜 해서 기간안에 있을때 더 할 수 있음
#이해가 잘 안갔다...

n = int(input())
dp = [0] * (n+1)
t = []
p = []
max_val = 0

for i in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)


#뒤에부터 접근
for i in range(n-1,-1,-1):
  time = t[i] + i
  #상담이 기간안에 끝나는 경우
  if time <= n:
    #현재까지의 최고 이익 계산
    dp[i] = max(p[i]+dp[time], max_val)
    max_val = dp[i]
  #상담이 기간을 벗어나는 경우
  else:
     dp[i] = max_val
print(max_val)