import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
S = set()

for _ in range(n):
  command = input()
  if command == 'all':
    S.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  elif command == 'empty':
    S = set()
  else:
    command, num = command.split()
    num = int(num)
    if command == 'add':
      S.add(num)
    elif command == 'remove':
      S.discard(num)
    elif command == 'check':
      if num in S:
        print(1)
      else:
        print(0)
    elif command == 'toggle':
      if num in S:
        S.remove(num)
      else:
        S.add(num)