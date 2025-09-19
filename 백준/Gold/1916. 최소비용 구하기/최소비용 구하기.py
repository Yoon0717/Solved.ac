import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input()) # 도시 수
m = int(input()) # 버스 수

# 출발 도시 번호, 도착 도시 번호, 버스 비용
graph = [[] for i in range(n+1)]
for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end,cost))

start, end = map(int, input().split())

dist = [float('inf') for _ in range(n+1)]
dist[start] = 0

queue = [(0, start)]

while queue:
  cur_dist, cur_idx = heapq.heappop(queue)
  if cur_dist > dist[cur_idx]: # 현재 비용보다 비싸면 필요없음
    continue
  for next_idx, next_dist in graph[cur_idx]:
    add_dist = cur_dist + next_dist
    if add_dist < dist[next_idx]: # 다음 비용보다 싸야 봄
      dist[next_idx] = add_dist
      heapq.heappush(queue, (add_dist, next_idx))

print(dist[end])