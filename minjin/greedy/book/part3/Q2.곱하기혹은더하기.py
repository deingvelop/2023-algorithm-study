# 풀이 1 - 더 효율적인 풀이
numbers = list(map(int, input()))
answer = 0

for num in numbers:
    answer = max(answer + num, answer * num)

print(answer)

# 풀이 2 - 교재 참고
numbers = list(map(int, input()))
answer = 0

for num in numbers:
    if answer <= 1 or num <= 1:
        answer += num
    else:
        answer *= num
    print(num, answer)

print(answer)