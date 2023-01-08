# 시도 1 - 정확성은 맞으나 시간초과(오답)
# 배운 것 - remove보다 del이 더 빠르다
def solution(people, limit):
    cnt = 0

    people.sort()

    while people:
        min_person = people[0]
        max_person = people[-1]
        if max_person + min_person > limit or len(people) == 1:
            del people[-1]
        else:
            del people[0], people[-1]
        cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))


# 풀이 1 - deque 사용
# 배운 것 - pop(0) 대신 popleft를 썼다. deque의 popleft는 O(1)이다.
#          리스트의 양 옆에서 원소를 가져올 일이 있으면 deque를 쓰자.
#        - 함수 안에서도 import 할 수 있다.

def solution(people, limit):
    from collections import deque

    people.sort()
    people = deque(people)
    answer = 0

    while people:
        if len(people) == 1:
            answer += 1
            break
        else:
            if people[0] + people[-1] > limit:
                people.pop()
            else:
                people.popleft()
                people.pop()
            answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))


# 풀이 2 - 투포인터
def solution(people, limit):

    people.sort()

    cnt = 0
    light_idx = 0
    heavy_idx = len(people) - 1

    while heavy_idx >= light_idx:
        if heavy_idx != light_idx and people[light_idx] + people[heavy_idx] <= limit:
            light_idx += 1
            heavy_idx -= 1
        else:
            heavy_idx -= 1
        cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))