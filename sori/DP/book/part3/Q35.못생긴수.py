#못생긴수
# 2,3,5만을 소인수로 가지는 수 배열 만들기.

n = int(input())
ugly = [0] * n
ugly[0] = 1 #첫번째 못생긴 수는 1

# * 못생긴수에 2,3,5 곱한 수 또한 못생긴 수이다.
# 바텀업 방식으로 1에 못생긴수 곱해가며 소인수 배열 만들기

#2배, 3배, 5배 인덱스
i2 = i3 = i5 = 0
#처음 곱셈값 초기화
next2, next3, next5 = 2,3,5

for i in range(1, n):
 # print("next2, next3, next5 " ,next2, next3, next5)
  ugly[i] = min(next2, next3, next5)
               #1st : 2, 3, 5
               #2nd : 4, 3, 5
  if ugly[i] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
  if ugly[i] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
  if ugly[i] == next5:
    i5 += 1
    next5 = ugly[i5] * 5
  #elif 로 하면 안됨. 공통 인수가 있기 때문에

print(ugly[n-1])
  