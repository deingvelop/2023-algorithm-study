# n: 행의개수, m:열의 개수 (1<=n,m<=100)
# 각 숫자 1이상 10000이하
# 각 행의 가장 작은 수 중에서 가장 큰수 고르기

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_val = min(data)
  if(min_val > result):
    result = min_val
  

print(result)

#if문 부분을 max(result, min_val)로 하면 더 쉽게 큰 값 비교가능