import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
n, k = map(int, input().split())

size = max(n, k)+2 # 인덱스 고려해서+1, 현재위치-1까지 고려해서 max+1의 +1
position = [0 for _ in range(size)] # 각 위치까지 가는데 걸리는 최소 시간
dq = deque([]) # 현재 위치에 대한 큐
dq.append(n)

while True:
    now = dq.popleft() # bfs
    if now == k:
        break
    for next in [now-1, now+1, now*2]: # 모든 경우
        if 0 <= next < size and position[next] == 0: # 범위 내에서 접근한 적이 없는 경우
            dq.append(next)
            position[next] = position[now]+1 # 다음 위치는 현재+1 시간

print(position[k])