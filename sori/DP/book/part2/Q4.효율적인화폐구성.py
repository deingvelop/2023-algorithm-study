#효율적인 화폐 구성
n, m = map(int, input().split())
array = []
d = [10001] * (m+1)

for i in range(n):
  array.append(int(input()))
d[0] = 0

for i in range(n):
  for j in range(array[i],m+1): #array[i]는 화폐단위
    d[j] = min(d[j], d[j-array[i]]+1)
    
if d[m] == 10001:
  print(-1)
else:
  print(d[m])