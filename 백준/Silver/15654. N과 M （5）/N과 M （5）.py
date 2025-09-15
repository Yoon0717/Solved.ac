import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

seq = []
def dfs():
  if len(seq) == m:
    print(' '.join(map(str, seq)))
    return
  
  for i in range(0, n):
    if nums[i] not in seq:
      seq.append(nums[i])
      dfs()
      seq.pop()

dfs()