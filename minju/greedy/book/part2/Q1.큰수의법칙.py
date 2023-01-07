n,m,k = map(int, input().split())
data = list(map(int, input().split()))

result = 0 

data.sort(reverse=True)

result = ((m//k)*k*data[0]) + ((m%k)*data[1])
print(result)
