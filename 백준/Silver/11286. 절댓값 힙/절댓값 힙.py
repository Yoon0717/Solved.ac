import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
  k = int(input())
  if k == 0:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap)[1])
  else:
    heapq.heappush(heap, (abs(k), k))
