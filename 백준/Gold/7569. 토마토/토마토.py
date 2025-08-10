import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

m, n, h = map(int, input().split()) # 가로, 세로, 높이(x, y, z)
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 1:
        q.append((z, y, x))

while q:
  z, y, x = q.popleft()
  for i in range(6):
    nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
    if 0<= nx < m and 0<= ny < n and 0<= nz < h:
      if graph[nz][ny][nx] == 0:
        graph[nz][ny][nx] = graph[z][y][x] + 1
        q.append((nz, ny, nx))

complete = True
day = 0

for z in range(h):
  for y in range(n):
    for x in range(m):
      if graph[z][y][x] == 0:
        complete = False
      day = max(day, graph[z][y][x])

if complete:
  print(day-1)
else:
  print(-1)