import sys
input = lambda : sys.stdin.readline().rstrip()

k = int(input())
li = []

for _ in range(k):
    n = int(input())
    if n == 0 and len(li) != 0:
        li.pop()
    else:
        li.append(n)

print(sum(li))