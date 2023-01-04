#n이 1이 될 때까지 전체 과정 실행 횟수 구하기
#1. n-1
#2. n/k (나누어 떨어질때만 n%k == 0)

n, k = map(int, input().split())
result = 0

while n>=k:
    while n%k!=0:
      n -= 1
      result += 1
    n //= k
    result += 1
      

while n>1:
  n-=1
  result += 1

print(result)