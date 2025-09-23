# 시작점이 0인 경우, 계속해서 0이 입력으로 들어감 -> 99%에서 틀림

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
size = 100001
dist = [float('inf')] * size
dist[n] = 0

def bfs(n, k):
  q = deque([n])
  while q:
    cur = q.popleft()
    if cur == k:
      print(dist[cur])
      return
    
    next = cur*2
    if 0 <= next < size and dist[next] > dist[cur]:
      dist[next] = dist[cur]
      q.appendleft(next)
    
    for next in [cur-1, cur+1]:
      if 0 <= next < size and dist[next] > dist[cur]+1:
          dist[next] = dist[cur]+1
          q.append(next)

if n == k:
  print(0)
else:
  bfs(n, k)