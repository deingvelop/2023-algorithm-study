N, M = list(map(int, input().split()))
arr = list(map(int, input(). split()))

answer = 0
max_arr = max(arr)
answer += (N*(N-1)//2) # nC2

for a in range(1, max(arr)+1):
    n_a = arr.count(a)
    answer -= (n_a*(n_a-1)//2)

print(answer)
