import sys
from collections import deque
sys.setrecursionlimit = 100000
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

# 방문 여부
visited = [[False] * m for _ in range(n)]

# 도연이 시작 위치
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start_x, start_y = i, j
            break

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((start_x, start_y))
visited[start_x][start_y] = True
count = 0

while queue:
    x, y = queue.popleft()
    if campus[x][y] == 'P':
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and campus[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx,ny))

print(count if count > 0 else 'TT')