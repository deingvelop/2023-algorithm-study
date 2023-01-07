from itertools import combinations

n = int(input())
data = list(map(int, input().split()))

c = []
for i in range(1,n+1):
  for x in (combinations(data, i)):
    c.append(sum(x))

c = list(set(c))

for i,a in enumerate(c):
  if i+1 != a :
    print(i+1)
    break
