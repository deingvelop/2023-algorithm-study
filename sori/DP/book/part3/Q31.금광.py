#금광
t = int(input())


def gold():
  n, m = map(int, input().split())
  array = list(map(int, input().split()))


  d = []
  index = 0
  for i in range(n):
    d.append(array[index:index+m])
    index += m
    
  for i in range(1,m):
    for j in range(n):
        max_val = d[j][i] 
        #왼쪽 위에서 올 때
        if 0<= j-1<n and 0 <= i-1 < m: 
          max_val = max(max_val, d[j-1][i-1] + d[j][i])
        #왼쪽에서 올 때
        if 0<= j <n and 0 <= i-1 < m: 
          max_val = max(max_val, d[j][i-1] + d[j][i])
        #왼쪽 아래에서 올 때
        if 0<= j+1 <n and 0 <= i-1 < m: 
          max_val = max(max_val, d[j+1][i-1] + d[j][i])
       
        d[j][i] = max_val

  return max(map(max, d))


result = []
for i in range(t):
  result.append(gold())

for j in range(t):
  print(result[j])