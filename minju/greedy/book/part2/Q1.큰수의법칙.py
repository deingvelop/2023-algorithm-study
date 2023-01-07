"""순서 상관 없이 큰 수 2개만 사용해서 조합"""

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

result = 0 

data.sort(reverse=True) #내림차순 정렬

result = ((m//k)*k*data[0]) + ((m%k)*data[1]) #가장큰 수를 최대한 사용하고, 그 다음 큰수를 나머지만큼 사용
print(result)
