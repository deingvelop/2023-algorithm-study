N, M = map(int, input().split())

cards = [ list(map(int, input().split())) for i in range(N) ]

answer = 1
for card in cards:
	if answer < min(card):
		answer = min(card)
		print(answer)
