import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, b = map(int, input().split()) # (n, m)땅과 b개의 블록을 가지고 시작
land = [list(map(int, input().split())) for _ in range(n)]

best_time, best_height, max_land_height = float('inf'), 0, max(map(max, land))

for target_height in range(max_land_height+1):
  time = 0
  block = b
  
  for i in range(n):
    for j in range(m):
      current_height = land[i][j]
      if current_height > target_height: # 블록을 깎아야 함
        time += 2 * (current_height - target_height)
        block += (current_height - target_height)
      else: # 블록을 쌓거나 유지해야 함
        time += (target_height - current_height)
        block -= (target_height - current_height)
  
  if block >= 0 and time <= best_time:
    best_time = time
    best_height = target_height

# 출력은 필요한 시간과 평평해진 땅의 높이 (깎는 것은 2초, 쌓는 것은 1초)
print(best_time, best_height)