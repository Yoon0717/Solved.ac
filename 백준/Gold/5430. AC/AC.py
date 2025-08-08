import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
  p = input() # AC함수
  n = int(input()) # 리스트 길이
  
  arr = input()[1:-1]
  if not arr:
    arr = deque()
  else:
    arr = deque(map(int, arr.split(',')))
  
  reverse = 0
  is_error = False
  
  for order in p:
    if order == 'R':
      reverse += 1
    elif order == 'D':
      if not arr:
        is_error = True
        break
      
      if reverse % 2 == 0:
        arr.popleft()
      else:
        arr.pop()
  
  if is_error:
    print('error')
    continue
  
  if reverse % 2 != 0:
    arr.reverse()
  print('[' + ','.join(map(str, arr)) + ']')