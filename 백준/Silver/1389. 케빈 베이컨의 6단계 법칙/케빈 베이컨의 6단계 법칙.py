import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split()) # 유저, 관계
graph = [[] for _ in range(n+1)] # i와 관계가 있는 [i]
min_distance = float('inf')

def bfs(start, graph, n):
  visited = [False] * (n+1)
  distance = [0] * (n+1)
  queue = deque() # queue = deque([start])
  queue.append(start)
  visited[start] = True
  
  while queue:
    now = queue.popleft()
    for next in graph[now]:
      if visited[next] is False:
        queue.append(next)
        distance[next] = distance[now]+1
      visited[next] = True
      
  total_distance = sum(distance)
  return total_distance

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, n+1):
  total_distance = bfs(i, graph, n)
  if total_distance < min_distance:
    # print(f'i={i}, min_distance={min_distance}, total_distance={total_distance}')
    min_distance = total_distance
    ans = i

print(ans)