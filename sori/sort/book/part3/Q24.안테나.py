#특정 위치의 집에 안테나 설치
#안테나로부터 모든 집까지의 거리의 총합이 최소
n = int(input())
house = list(map(int, input().split()))

house.sort()

min_value = 0

arr = []
for i in house:
  amount = 0
  for j in house:
    amount += abs(i-j)
  arr.append((i, amount))

arr = sorted(arr, key=lambda x:(x[1],x[0]))

print(arr[0][0])

#책 풀이
n = int(input())
house = list(map(int, input().split()))

house.sort()

#중간 값을 출력
print(house[(n-1)//2])