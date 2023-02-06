#열+행으로 입력값을 받음 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #문자열을 숫자값으로 바꾸기

move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] #이동할 수 있는 모든 경우의 수

can = 0
for i in range(len(move)):
  if row+(move[i][0])>=1 and row+(move[i][0])<=8 and column+(move[i][1])>=1 and column+(move[i][1]) <= 8 :
    can = can +1 

print(can)
