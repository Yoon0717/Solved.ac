import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
li = []
for _ in range(n):
  command = input()
  if ' ' in command:
    command, num = command.split()
    num = int(num)
  if command == 'push':
    li.append(num)
  elif command == 'pop':
    if len(li) == 0:
      print(-1)
    else:
      print(li.pop())
  elif command == 'size':
    print(len(li))
  elif command == 'empty':
    if len(li) == 0:
      print(1)
    else:
      print(0)
  elif command == 'top':
    if len(li) == 0:
      print(-1)
    else:
      print(li[-1])