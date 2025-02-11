import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

min_heap = []
n = int(input())

for _ in range(n):
    h = int(input())
    if h == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, h)
        