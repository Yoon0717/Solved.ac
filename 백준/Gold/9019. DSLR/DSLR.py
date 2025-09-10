# import sys
# from collections import deque
# input = lambda : sys.stdin.readline().rstrip()

# def D(k):
#   return (k * 2) % 10000

# def S(k):
#   return 9999 if k == 0 else k - 1

# def L(k):
#   return (k % 1000) * 10 + (k // 1000)

# def R(k):
#   return (k % 10) * 1000 + (k // 10)

# ops = {
#   'D': D,
#   'S': S,
#   'L': L,
#   'R': R
# }

# T = int(input())

# for _ in range(T):
#   A, B = map(int, input().split())
  
#   visited = [False] * 10000 # 0 ~ 9999 범위에서 움직임
  
#   q = deque([A])
#   visited[A] = True
#   prev = [-1] * 10000 # prev[next] = prev
#   how = [''] * 10000 # prev + how[next] = next
  
#   while q:
#     x = q.popleft()
#     if x == B:
#       break
#     for op in ['D', 'S', 'L', 'R']:
#       nx = ops[op](x)
#       if not visited[nx]:
#         visited[nx] = True
#         prev[nx] = x
#         how[nx] = op
#         q.append(nx)
  
#   path = ''
#   while A != B:
#     path = how[B] + path
#     B = prev[B]
#   print(path)

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  visited = [False] * 10000 # 0 ~ 9999 범위에서 움직임
  q = deque()
  q.append((A, ''))
  visited[A] = True
  
  while q:
    num, operation = q.popleft()
    
    if num == B:
      print(operation)
      break
    
    d = num * 2 % 10000
    if not visited[d]:
      visited[d] = True
      q.append((d, operation + 'D'))
    
    s = (num + 9999) % 10000
    if not visited[s]:
      visited[s] = True
      q.append((s, operation + 'S'))
    
    l = (num % 1000) * 10 + (num // 1000)
    if not visited[l]:
      visited[l] = True
      q.append((l, operation + 'L'))
    
    r = (num % 10) * 1000 + (num // 10)
    if not visited[r]:
      visited[r] = True
      q.append((r, operation + 'R'))