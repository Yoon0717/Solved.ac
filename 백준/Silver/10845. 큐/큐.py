import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dq = deque()
for _ in range(n):
  command = input()
  if ' ' in command:
    command, num = command.split()
    num = int(num)
  if command == 'push':
    dq.append(num)
  elif command == 'pop':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq.popleft())
  elif command == 'size':
    print(len(dq))
  elif command == 'empty':
    if len(dq) == 0:
      print(1)
    else:
      print(0)
  elif command == 'front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
  elif command == 'back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[-1])