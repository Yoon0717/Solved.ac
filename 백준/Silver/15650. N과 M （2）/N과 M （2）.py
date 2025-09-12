import sys
input = lambda : sys.stdin.readline().rstrip()

n ,m = map(int, input().split())
seq = []

def dfs(start):
  if len(seq) == m:
    print(' '.join(map(str, seq)))
    return
  
  for i in range(start, n+1):
    if i not in seq:
      seq.append(i)
      dfs(i+1)
      seq.pop()

dfs(1)