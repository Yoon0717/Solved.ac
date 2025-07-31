import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def dfs(k, t):
  visited.append(t)
  for i in point[t]:
    line[k][i] = 1
    if i not in visited:
      dfs(k, i)

n = int(input())
point = {i:[] for i in range(n)}

for i in range(n):
  k = list(map(int, input().split()))
  for j in range(len(k)):
    if k[j] == 1:
      point[i].append(j)

line = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  visited = []
  dfs(i, i)

for l in line:
  print(*l)