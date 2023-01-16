from itertools import combinations

N, M = map(int, input().split())

homes = []
chickens = []

for i in range(N):
    city = list(map(int, input().split()))

    for j in range(N):
        if city[j] == 1: # home
            homes.append([i,j])
        elif city[j] == 2 : # chicken
            chickens.append([i,j])

possible_chickens = list(combinations(chickens, M))

city_chicken_distance = 50*2*N
for possible_chicken in possible_chickens:
    chicken_distances = []
    
    # possible_chicken = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    for home in homes:
        # home = (0,2)

        chicken_distance = 2*N
        for chicken in possible_chicken:
            chicken_distance = min( chicken_distance, 
            abs(home[0]-chicken[0]) + abs(home[1]-chicken[1]) )
        
        chicken_distances.append(chicken_distance)
    city_chicken_distance = min(city_chicken_distance,
    sum(chicken_distances))
    
print(city_chicken_distance)
