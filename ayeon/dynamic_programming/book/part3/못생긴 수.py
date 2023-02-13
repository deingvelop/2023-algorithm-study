import sys

n = int(sys.stdin.readline())

ugly = [0] * n # 못생긴 수
ugly[0] = 1

# 몇 번째 인덱스까지 2,3,5 배한 결과를 다뤘는지
i2 = i3 = i5 = 0

# 다음으로 다뤄야 하는 곱셈 값
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for i in range(1,n):
   
    # 다음으로 다뤄야하는 곱셈 값들 중, 최솟값을 i번째 인덱스에 저장
    ugly[i] = min(next2, next3, next5)
    
    # next2 에 2를 곱한 값 저장
    if ugly[i] == next2:
      i2 += 1
      next2 = ugly[i2]*2
      
    # next3 에 3을 곱한 값 저장
    if ugly[i] == next3:
      i3 += 1
      next3 = ugly[i3]*3
      
    # next5에 5를 곱한 값 저장
    if ugly[i] == next5:
      i5 += 1
      next5 = ugly[i5]*5
      
print(ugly[n-1])
