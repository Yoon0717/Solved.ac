import sys
input = lambda : sys.stdin.readline().rstrip()

sen = input()
bomb = input()

stack = []
for s in sen:
  stack.append(s)
  if ''.join(stack[-len(bomb):]) == bomb:
    for _ in range(len(bomb)):
      stack.pop()

if stack:
  print(''.join(stack))
else:
  print('FRULA')