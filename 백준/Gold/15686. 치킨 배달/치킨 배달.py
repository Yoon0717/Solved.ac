import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n, m = map(int, input().split()) # NxN 크기, M개까지만 살리기

house = [] # 1
chicken = [] # 2
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 1:
      house.append((i,j))
    elif line[j] == 2:
      chicken.append((i,j))

min_dist = float('inf')
# visited = [False] * len(chicken)

# 치킨 집을 선택 -> count + 1
# 해당 치킨 집과 모든 집과의 거리를 구해서 list로 넘겨줌
# 현재 갖고 있는 치킨거리와 list 거리를 비교해서 min 값으로 업데이트
# count == m 이면 치킨거리 합과 min_dist 비교해서 min 값으로 업데이트 후 Return

def dfs(dist, count): 
  global min_dist
  if count == m:
    min_dist = min(min_dist, sum(dist))
    return
  
  for i in range(count, len(chicken)-m+count+1): # 여기서 i는 현재 고른 치킨 집
    x1, y1= chicken[i] # 고른 치킨집
    new_dist = [0] * len(house)
    for j in range(len(house)): # 치킨 거리 비교
      x2, y2 = house[j]
      comp_dist = abs(x1-x2) + abs(y1-y2)
      new_dist[j] = min(dist[j], comp_dist)
    count += 1
    dfs(new_dist, count)
    count -= 1

init_dist = [float('inf')] * len(house)
dfs(init_dist, 0)

print(min_dist)