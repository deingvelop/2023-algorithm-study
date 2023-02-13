# 정수 삼각형

n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

for i in range(1,n):
  
  for j in range(i+1):
    max_val = 0
    #왼쪽 대각선
    if 0<= i-1<n and 0<=j-1<i:
      max_val = max(max_val, arr[i-1][j-1] +arr[i][j])
    #오른쪽 대각선
    if 0<= i-1<n and 0<=j<i:   
      max_val = max(max_val, arr[i-1][j] +arr[i][j])
    
    arr[i][j] = max_val

print(arr)
print(max(map(max,arr)))
