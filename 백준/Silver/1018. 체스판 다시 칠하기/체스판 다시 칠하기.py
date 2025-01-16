import sys
from math import inf
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = []
min_map = inf

for _ in range(n):
  board.append(input())

for i in range(n-7):
  for j in range(m-7):
    black_start = 0
    white_start = 0
  
    for x in range(i, i+8):
      for y in range(j, j+8):
        if (x+y) % 2 == 0:
          if board[x][y] != 'B':
            black_start += 1
          if board[x][y] != 'W':
            white_start += 1
        else:
          if board[x][y] != 'W':
            black_start += 1
          if board[x][y] != 'B':
            white_start += 1
    
    if min_map > min(black_start, white_start):
      min_map = min(black_start, white_start)

print(min_map)