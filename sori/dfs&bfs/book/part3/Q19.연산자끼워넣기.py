from itertools import product


#각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우에 대하여 만들어질 수 있는 결과의 최댓값과 최솟값 구하기.
#-> 모든 경우의 수를 계산 : DFS, BFS 사용 또는 중복순열(product)사용
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

#print(product_list)

l = list()
for i in range(add):
    l.append('+')
for i in range(sub):
    l.append('-')
for i in range(mul):
    l.append('*')
for i in range(div):
    l.append('/')
print(l)

product_list = list(product(l, repeat= (n-1)))
print(product_list)
#최솟값, 최댓값 초기화(-10억~10억)
min_val = 1e9
max_val = -1e9
min_value = 1e9
max_value = -1e9

for cal in product_list:

  result = data[0]
  for i in range(n-1):
    if cal[i] == '+' :
      result = result + data[i+1]
    if cal[i] == '-' :
      result = result - data[i+1]
    if cal[i] == '*' :
      result = result * data[i+1]
    if cal[i] == '/' :
      result = int(result / data[i+1])
  
  min_value = min(min_value,result)
  max_value = max(max_value,result)

print(max_value)    
print(min_value)   

def dfs(i, now):
    global min_val, max_val,add, sub, mul, div
    #모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n :
        min_val = min(min_val,now)
        max_val = max(max_val,now)
    else:
        #각 연산자에 대하여 재귀적으로 수행
        if add > 0 :
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i])) #나눌 때는 나머지를 제거
            div += 1
    
#DFS 메서드 호출
dfs(1,data[0])
                
#최댓값과 최솟값 차례대로 출력
print(max_val)    
print(min_val)                
