import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split()) # 정점 수, 간선 수
k = int(input()) # 시작점
distance = [float('inf')] * (v+1)

graph = [[] for _ in range(v+1)]
for _ in range(e):
  start, end, cost = map(int, input().split())
  graph[start].append((end,cost))

q = []
heapq.heappush(q, (0,k))
distance[k] = 0
while q:
  dist, now = heapq.heappop(q)
  
  if distance[now] < dist:
    continue
  
  for g in graph[now]:
    next = g[0]
    cost = dist + g[1]
    
    if distance[next] > cost:
      distance[next] = cost
      heapq.heappush(q, (cost, next))

for i in range(1, v+1):
  if distance[i] == float('inf'):
    print("INF")
  else:
    print(distance[i])