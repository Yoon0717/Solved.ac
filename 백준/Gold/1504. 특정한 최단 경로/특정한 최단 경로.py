import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n, e = map(int, input().split()) # 1번에서 n번까지 가야 함
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split()) # a와 b 사이의 길이 = c
  graph[a].append((b,c))
  graph[b].append((a,c))

v1, v2 = map(int, input().split()) # 경로에 v1과 v2가 존재해야 함

def dijkstra(start):
  distance = [float('inf')] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
      continue
    
    for g in graph[now]:
      cost = dist + g[1]
      next = g[0]
      
      if distance[next] > cost:
        distance[next] = cost
        heapq.heappush(q, (cost, next))
  return distance

origin_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_v2 = origin_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_v1 = origin_distance[v2] + v2_distance[v1] + v1_distance[n]

answer = min(v1_v2, v2_v1)

if answer == float('inf'):
  answer = -1

print(answer)