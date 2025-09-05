import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())

jump = [i for i in range(101)]
for _ in range(n+m):
  s, e = map(int, input().split())
  jump[s] = e

dist = [-1] * 101
dq = deque([1])
dist[1] = 0

while dq:
  current = dq.popleft()
  if current == 100:
    print(dist[current])
    break
  for i in range(1, 7):
    if current+i <= 100:
      next = jump[current+i]
      if dist[next] == -1:
        dist[next] = dist[current] + 1
        dq.append(next)