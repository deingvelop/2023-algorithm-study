# 나의 풀이
n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

answer = 0
# answer = sum(a_list)
# b_max_log = 0
# a_min_log = 99999999
for _ in range(k):
    a_min_tmp = min(a_list)
    b_max_tmp = max(b_list)
    if b_max_tmp - a_min_tmp >= 0:
        b_list[b_list.index(b_max_tmp)], a_list[a_list.index(a_min_tmp)] = a_min_tmp, b_max_tmp
    else:
        break

print(sum(a_list))



# 교재 풀이 - 더 깔끔
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))