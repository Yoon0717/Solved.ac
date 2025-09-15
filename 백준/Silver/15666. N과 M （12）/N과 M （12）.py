import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []

def dfs(start_index):
  check = 0
  if len(ans) == m:
    print(*ans)
    return
  
  for i in range(start_index, n):
    if check != nums[i]:
      check = nums[i]
      ans.append(nums[i])
      dfs(i)
      ans.pop()

dfs(0)