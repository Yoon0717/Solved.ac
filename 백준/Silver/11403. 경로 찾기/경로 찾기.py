import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)] # 이미 갈 수 있는 길을 내포하므로, 이 내용을 활용하는게 좋음

for k in range(n):
  for i in range(n):
    if graph[i][k]: # i->k가 된다면
        for j in range(n):
          if graph[k][j]: # k->i가 된다면
            graph[i][j] = 1 # i->j가 된다

for g in graph:
  print(*g)