import sys
# sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 1
visited = [False] * 26

def idx(alp):
  return ord(alp) - 65

def dfs(x, y, cnt):
  global answer
  if cnt > answer:
    answer = cnt
  
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0 <= nx < R and 0 <= ny < C:
      n_alpha = board[nx][ny]
      if not visited[idx(n_alpha)]:
        visited[idx(n_alpha)] = True
        dfs(nx, ny, cnt+1)
        visited[idx(n_alpha)] = False

visited[idx(board[0][0])] = True
dfs(0,0,1)
print(answer)