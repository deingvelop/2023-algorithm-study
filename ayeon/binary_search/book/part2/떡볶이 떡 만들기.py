import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ddeok = list(map(int, input().split()))

def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start+end) // 2

        s = 0
        for a in arr:
            if a > mid:
                s += a - mid
        
        if s < target:
            end = mid -1
        else:
            answer = mid 
            start = mid +1
    
    return answer

ddeok.sort()
print(binary_search(ddeok, 6, ddeok[0], ddeok[-1]))
