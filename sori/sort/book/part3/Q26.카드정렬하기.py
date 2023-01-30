import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)
result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sumVal = one + two
    result += sumVal
    heapq.heappush(heap, sumVal)
                   
print(result)

#그리디와 우선순위 큐를 생각하면 쉽게 풀수 있음.
#힙 자료구조 사용법 알기 
'''
import heapq
힙에 넣기 : heapq.heappush(heap,data)
힙에서 꺼내기 : heapq.heappop(heap)

'''