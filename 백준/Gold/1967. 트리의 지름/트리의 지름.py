import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  x, y, dist = map(int, input().split())
  graph[x].append((y, dist))
  graph[y].append((x, dist))

def dfs(start, dist):
  for next_node, next_dist in graph[start]:
    if visited[next_node] == -1:
      visited[next_node] = dist + next_dist
      dfs(next_node, dist+next_dist)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

node = visited.index(max(visited))

visited = [-1] * (n+1)
visited[node] = 0
dfs(node, 0)

print(max(visited))