import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
picture = [list(input()) for _ in range(n)]
normal, unnormal = 0, 0

dq = deque()
visited_normal = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
  for j in range(n):
    if not visited_normal[i][j]:
      dq.append((i,j))
      color = picture[i][j]
      normal += 1
      while dq:
        x, y = dq.popleft()
        if not visited_normal[x][y]:
          visited_normal[x][y] = True
          for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n: # 범위 내 인덱스
              if color == picture[nx][ny]: # 같은 색깔에 대해서만 방문
                dq.append((nx, ny))

# print(normal)

dq = deque()
visited_unnormal = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if not visited_unnormal[i][j]:
      dq.append((i,j))
      color = picture[i][j]
      if color == 'R' or color == 'G':
        color = 'RG'
      unnormal += 1
      while dq:
        x, y = dq.popleft()
        if not visited_unnormal[x][y]:
          visited_unnormal[x][y] = True
          for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n: # 범위 내 인덱스
              # if picture[nx][ny] == 'R' or picture[nx][ny] == 'G':
              #   comp_color = 'RG'
              # else:
              #   comp_color = 'B'
              if picture[nx][ny] in color: # 같은 색깔에 대해서만 방문
                dq.append((nx, ny))

print(normal, unnormal)