import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
  line = list(map(int, input().split()))
  if 2 in line:
    j = line.index(2)
    start_i = i
    start_j = j
  graph.append(line)

start = (start_i, start_j)
queue = deque([start])
visited = set()
visited.add(start)

score = [[0 for _ in range(m)] for _ in range(n)] # 최종 출력
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

while queue:
  i, j = queue.popleft()
  for k in range(4):
    next_i, next_j = i+dy[k], j+dx[k]
    if (next_i >= 0 and next_i < n) and (next_j >=0 and next_j < m):
      neighbor = (next_i, next_j)
      if neighbor not in visited and graph[next_i][next_j]:
        score[next_i][next_j] = score[i][j] + 1
        queue.append(neighbor)
        visited.add(neighbor)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and score[i][j] == 0:
      score[i][j] = -1

for s in score:
  print(*s)