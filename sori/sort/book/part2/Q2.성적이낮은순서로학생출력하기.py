#성적이 낮은 순서대로 학생 이름 출력(오름차순)
n = int(input())
array = []
for i in range(n):
  name, score = input().split()
  array.append((name,int(score)))

array = sorted(array, key=lambda x:x[1])

for i in array:
  print(i[0], end=' ')

#sorted key= lambda 참고
tuple_list = [('좋은하루', 0),
    	          ('niceday', 1), 
    	          ('좋은하루', 5), 
    	          ('good_morning', 3), 
    	          ('niceday',5)]
                  
tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
print(tuple_list)
#[('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]