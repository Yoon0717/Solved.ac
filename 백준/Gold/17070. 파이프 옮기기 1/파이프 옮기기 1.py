import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 좌표와 방향을 넣어줌
# (3,n,n) 공간 생성
# 0:가로 (0, i, j), 1:세로 (1, i, j), 2:대각선 (2, i, j)

dp[0][0][1] = 1
for i in range(2, n):
  if house[0][i] == 0:
    dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
  for j in range(1, n):
    if house[i][j] == 0 and house[i-1][j] == 0 and house[i][j-1] == 0: # 대각선 추가
      dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
    
    if house[i][j] == 0: # 가로,세로 추가
      dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
      dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(sum(dp[i][n-1][n-1] for i in range(3)))

# import sys
# from collections import deque
# input = lambda : sys.stdin.readline().rstrip()

# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]

# dq = deque()
# dq.append((0,1,1))
# answer = 0

# while dq:
#   i, j, pose = dq.popleft()
  
#   if i == n-1 and j == n-1:
#     answer += 1
#     continue
  
#   if pose == 1:
#     if j+1 < n and house[i][j+1] != 1:
#       dq.append((i, j+1, 1))
#     if i+1 < n and j+1 < n and house[i][j+1] != 1 and house[i+1][j] != 1 and house[i+1][j+1] != 1:
#       dq.append((i+1, j+1, 3))
    
#   elif pose == 2:
#     if i+1 < n and house[i+1][j] != 1:
#       dq.append((i+1, j, 2))
#     if i+1 < n and j+1 < n and house[i][j+1] != 1 and house[i+1][j] != 1 and house[i+1][j+1] != 1:
#       dq.append((i+1, j+1, 3))
    
#   else:
#     if i+1 < n and j+1 < n and house[i][j+1] != 1 and house[i+1][j] != 1 and house[i+1][j+1] != 1:
#       dq.append((i+1, j+1, 3))
    
#     if j+1 < n and house[i][j+1] != 1:
#       dq.append((i, j+1, 1))
    
#     if i+1 < n and house[i+1][j] != 1:
#       dq.append((i+1, j, 2))

# print(answer)