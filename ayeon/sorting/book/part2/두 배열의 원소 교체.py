# 배열 A 의 모든 원소의 합이 최대가 되도록 하는 것

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 오름차순
B.sort(reverse=True) # 내림차순

for i in range(K):
    if A[i] >= B[i]:
        break
    else:
        A[i] = B[i]

print(sum(A))
