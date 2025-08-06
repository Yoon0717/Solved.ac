import sys
input = sys.stdin.readline

N, c, r = map(int, input().split())
n = 2**N
ans = 0

while n > 0:
  n //= 2
  if c < n and r < n:
    pass
  elif c < n and r >= n:
    ans += n * n * 1
    r -= n
  elif c >=n and r < n:
    ans += n * n * 2
    c -= n
  elif c >=n and r >= n:
    ans += n * n * 3
    c -= n
    r -= n

print(ans)