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


'''
처음 작성했던 코드
while n>=k:
  print(f"n:{n},k:{k},result:{result}")
  if n != 1:
    if n%k==0:
      n //= k
      result += 1
    elif n%k!=0:
      n -= 1
      result += 1
  if n == 1:
      break

k>n인 경우 과정 실행 안됨.
'''