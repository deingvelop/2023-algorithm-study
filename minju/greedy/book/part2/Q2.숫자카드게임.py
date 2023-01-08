n,m = map(int, input().split())

minlist = []

for i in range(n):
  data = list(map(int, input().split()))
  minlist.append(min(data))

print(max(minlist))
