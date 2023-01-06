#만들 수 없는 금액
a = int(input())
data = list(map(int, input().split()))

data.sort()
print(data)

target = 1
for i in data:
  if target < i:
    break
  else:
    print(target)
    target += i
    

print(target)