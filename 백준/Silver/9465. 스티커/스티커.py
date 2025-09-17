import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input()) # 테스트케이스
for _ in range(T):
  score = []
  n = int(input()) # 열 갯수
  for _ in range(2):
    score.append(list(map(int, input().split())))
  
  # 1. 전 열의 대각선 선택 (전 열의 같은 행은 불가능), 2. 전전열의 대각선 선택 (전전열의 같은 행을 선택하면 전 열의 대각선도 선택하는게 당연함)
  dp = [[0]*n for _ in range(2)]
  for i in range(n):
    if i == 0:
      dp[0][i] = score[0][i]
      dp[1][i] = score[1][i]
    elif i == 1:
      dp[0][i] = dp[1][i-1] + score[0][i]
      dp[1][i] = dp[0][i-1] + score[1][i]
    else:
      dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + score[0][i]
      dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + score[1][i]
  print(max(dp[0][-1], dp[1][-1]))