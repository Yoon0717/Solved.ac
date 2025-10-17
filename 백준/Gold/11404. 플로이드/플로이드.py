import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

INF = float('inf')
ans = [[INF]*(n+1) for _ in range(n+1)]
bus = {i:[] for i in range(1, n+1)}

for _ in range(m):
  start, end, cost = map(int, input().split())
  bus[start].append((end, cost))
  ans[start][end] = min(ans[start][end], cost)

for start in range(1, n+1):
  heap = []
  for k in bus[start]: # i:start, k:(cost, end)
    end, cost = k
    if ans[start][end] >= cost:
      heapq.heappush(heap, (cost, end))
  
  while heap:
    cost, current = heapq.heappop(heap)
    if cost > ans[start][current]:
      continue
    
    ans[start][current] = min(ans[start][current], cost)
    for k in bus[current]:
      next, next_cost = k
      next_cost += cost
      if ans[start][next] > next_cost:
        heapq.heappush(heap, (next_cost, next))

for i in range(1, n+1):
  for j in range(1, n+1):
    if ans[i][j] == INF or i==j:
      print(0, end=' ')
    else:
      print(ans[i][j], end=' ')
  print()