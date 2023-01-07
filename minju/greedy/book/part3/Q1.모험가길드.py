n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

cnt = 0
i = 0
x = 0

while i < n:
  x = data[i] #3 2 
  i =  i + x  #3 5
  cnt = cnt + 1

print(cnt)
