import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
sem = []

for i in range(n):
    a, b = map(int, input().split())
    sem.append((a,b))

sem.sort(key = lambda x : (x[1], x[0]))

count = 0
last = 0
for s in sem:
    if s[0] >= last:
        count += 1
        last = s[1]

print(count)