import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

A, B = map(int, input().split())
q = deque()
q.append((A, 1))

get_ans = False

while q:
  num, count = q.popleft()
  if num > B:
    continue
  if num == B:
    get_ans = True
    print(count)
    break
  q.append((num*2, count+1))
  q.append((num*10+1, count+1))

if not get_ans:
  print(-1)