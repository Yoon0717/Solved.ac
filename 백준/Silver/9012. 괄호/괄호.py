import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
  sen = input()
  li = []
  for s in sen:
    if s == '(':
      li.append(s)
    else:
      if len(li) != 0 and li[-1] == '(':
        li.pop()
      else:
        li.append(s)
        break
  if len(li) == 0:
    print('YES')
  else:
    print('NO')