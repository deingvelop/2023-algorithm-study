# 풀이 1 - 우선순위 큐 (교재)
import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로, 우선순위 큐를 이용
    queue = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(queue, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    prev_food_time = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식의 개수

    # (sum_value + ((현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수))와 k 비교
    while sum_value + ((queue[0][0] - prev_food_time) * length) <= k:
        now_food_time = heapq.heappop(queue)[0]
        sum_value += (now_food_time - prev_food_time) * length
        length -= 1  # 다 먹은 음식 제외
        prev_food_time = now_food_time  # 이전 음식 시간 재설정

    # 남은 음식 중 몇 번째 음식인지 확인하여 출력
    result = sorted(queue, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))



# 풀이 2 - 우선순위 큐 (https://kjhoon0330.tistory.com/12)
from heapq import heappush, heappop


def solution(food_times, k):
    # 더 섭취할 음식이 없다면 -1 반환
    if sum(food_times) <= k:
        return - 1

    # [음식 먹는 데에 걸리는 시간, 음식 번호]로 우선순위 큐 만들기
    foodHeap = []
    length = len(food_times)  # 남은 음식 개수
    for i in range(length):
        heappush(foodHeap, [food_times[i], i + 1]);

    # 남은 음식 중 가장 소요시간이 작은 음식을 먹을 정도로 충분히 돌 수 있다면,
    # 남은 시간(k) 갱신, 누적시간(time) 갱신, 남은 음식 개수(length) 갱신, 해당 음식(foodHeap[0]) 제거
    # => k를 한 바퀴 내의 숫자로 변환하는 과정
    time = 0
    while (foodHeap[0][0] - time) * length < k:
        k -= (foodHeap[0][0] - time) * length
        time += (foodHeap[0][0] - time)
        length -= 1
        heappop(foodHeap)

    # index를 기준으로 heap을 다시 정렬
    result = sorted(foodHeap, key=lambda x: x[1])
    answer = result[k % length][1]
    return answer


# 나의 풀이
from heapq import heappush, heappop


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    foodHeap = []
    for food_num in range(1, len(food_times) + 1):
        heappush(foodHeap, (food_times[food_num - 1], food_num))

    past_time = 0
    while (foodHeap[0][0] - past_time) * len(foodHeap) < k:
        k -= (foodHeap[0][0] - past_time) * len(foodHeap)
        past_time += (foodHeap[0][0] - past_time)
        # past_time = foodHeap[0][0]
        heappop(foodHeap)

    final_foods = sorted(foodHeap, key=lambda x: x[1])
    return final_foods[k % len(foodHeap)][1]


print(solution([3, 1, 2], 5))
