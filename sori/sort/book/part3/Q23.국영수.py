#국(내림차순), 영(오름차순), 수(내림차순), #이름(오름차순)
students = []
n = int(input()) #도현이네 반 학생 수
for i in range(n):
  name, korean, english, math = input().split()
  students.append((name, int(korean), int(english), int(math)))

students = sorted(students, key=lambda x:(-x[1],x[2],-x[3],x[0]))
  
for i in students:
  print(i[0])

'''
input
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''