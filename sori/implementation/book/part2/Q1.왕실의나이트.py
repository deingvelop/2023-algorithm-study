n = input()
data = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
x = int(n[1])
y = ord(n[0]) - ord('a') + 1
result = 0

for i in data:
  nx = x + i[0]
  ny = y + i[1]
  if(1<=nx<=8 and 1<=ny<=8):
    result += 1

print(result)