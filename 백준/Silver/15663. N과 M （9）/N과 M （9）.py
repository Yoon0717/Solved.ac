import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n # 동일한 인덱스 접근 제한
ans = []

def dfs():
  check = 0
  if len(ans) == m:
    print(*ans)
    return
  
  for i in range(n):
    if not visited[i] and check != nums[i]:
      ans.append(nums[i])
      visited[i] = True
      check = nums[i]
      dfs()
      ans.pop()
      visited[i] = False

dfs()