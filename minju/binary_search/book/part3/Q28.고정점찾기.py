n = int(input())
array = list(map(int,input().split()))

result = -1
for index, x in enumerate(array):
  if index == x:
    result = x
    break
    
print(result)
