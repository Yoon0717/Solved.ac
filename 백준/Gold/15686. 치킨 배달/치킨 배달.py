import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split()) # NxN 크기, M개 선택

house = []
chicken = []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 1:
      house.append((i,j))
    elif line[j] == 2:
      chicken.append((i,j))

combs = list(combinations(chicken, m))

min_dist = float('inf')
for comb in combs:
  dist = 0 # 모든 치킨집과 가정집 거리의 합
  for x1, y1 in house:
    sub_dist = float('inf') # 하나의 집과 하나의 치킨 집 거리 중 최솟값 구하기
    for x2, y2 in comb:
      one_dist = abs(x1-x2) + abs(y1-y2)
      sub_dist = min(sub_dist, one_dist)
    dist += sub_dist
  min_dist = min(min_dist, dist)

print(min_dist)

# min_dist = float('inf')

# def dfs(dist, count): 
#   global min_dist
#   if count == m:
#     min_dist = min(min_dist, sum(dist))
#     return
  
#   for i in range(count, len(chicken)-m+count+1): # 여기서 i는 현재 고른 치킨 집
#     x1, y1= chicken[i] # 고른 치킨집
#     new_dist = [0] * len(house)
#     for j in range(len(house)): # 치킨 거리 비교
#       x2, y2 = house[j]
#       comp_dist = abs(x1-x2) + abs(y1-y2)
#       new_dist[j] = min(dist[j], comp_dist)
#     count += 1
#     dfs(new_dist, count)
#     count -= 1

# init_dist = [float('inf')] * len(house)
# dfs(init_dist, 0)

# print(min_dist)