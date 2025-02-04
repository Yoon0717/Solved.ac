import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
count = 0

for i in range(n-1, -1, -1):
    count += k // coin[i]
    k %= coin[i]

print(count)