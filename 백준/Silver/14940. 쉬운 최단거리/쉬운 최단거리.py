import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
score = [[-1 for _ in range(m)] for _ in range(n)] # 출력용 (-1이면 아직 도달하지 않은 곳이거나(visited 필요 없음) 갈 수 없는 곳(-1 처리))

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(m):
    if line[j] == 2:
      start = (i, j)
      score[i][j] = 0
  graph.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([start])

while queue:
  i, j = queue.popleft()
  for k in range(4):
    ni, nj = i+dy[k], j+dx[k]
    if 0 <= ni < n and 0 <= nj < m:
      if graph[ni][nj] == 1 and score[ni][nj] == -1:
        score[ni][nj] = score[i][j] + 1
        queue.append((ni, nj))

for i in range(n):
  row = []
  for j in range(m):
    if graph[i][j] == 0:
      row.append(0)
    else:
      row.append(score[i][j])
  print(' '.join(map(str, row)))