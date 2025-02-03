import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

no_listen = set()
no_watch = set()

for _ in range(n):
  no_listen.add(input())

for _ in range(m):
  no_watch.add(input())

no_both = list(no_listen & no_watch)
no_both.sort()

print(len(no_both))

for k in no_both:
  print(k)