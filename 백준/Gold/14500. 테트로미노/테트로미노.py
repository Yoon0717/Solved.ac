import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
score_map = [list(map(int, input().split())) for _ in range(n)]

visited =[[False] * m for _ in range(n)]
max_value = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, depth, value):
  global max_value
  
  if depth == 4:
    max_value = max(max_value, value)
    return 
  
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx, ny, depth+1, value+score_map[nx][ny])
      visited[nx][ny] = False # 백트래킹

def check_mountain(x, y): # 해당 좌표에서 4가지로 갈 수 있음 -> 한 쪽을 빼면 ㅗ모양 가능
  global max_value
  
  for exclude in range(4): # 한 점에서 4방향 고려
    value = score_map[x][y]
    for k in range(4):
      if k == exclude: # 매 반복에서 한 방향은 제외
        continue
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        value += score_map[nx][ny]
    max_value = max(value, max_value)

for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i, j, 1, score_map[i][j])
    visited[i][j] = False
    check_mountain(i, j)

print(max_value)