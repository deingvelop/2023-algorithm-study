""" 시간초과 된 내 코드

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = []
for i in a:
    d.append([i,sum(list(map(lambda x: abs(i-x), a)))])
d.sort(key=lambda x: (x[1],x[0])) 
print(d[0][0])

"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[(n - 1) // 2])
