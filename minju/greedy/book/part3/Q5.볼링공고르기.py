from itertools import combinations
n,m = map(int, input().split())
k = list(map(int, input().split()))

all = list(combinations(k ,2))

cnt= 0
for i in range(len(all)):
  if all[i][0] != all[i][1] :
    cnt = cnt + 1

print(cnt)    
