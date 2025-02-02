import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

encyclopedia = {}
num = 1
for _ in range(n):
  name = input()
  encyclopedia[name] = num
  encyclopedia[num] = name
  num += 1

for _ in range(m):
  q = input()
  if q.isdigit():
    q = int(q)
    print(encyclopedia[q])
  else:
    print(encyclopedia[q])