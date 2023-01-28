n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    temp = b[i]
    a[i] = temp
  else: #A의 원소가 B의 원소보다 크거나 같을 때, 반복무을 탈출
    break
print(sum(a))
