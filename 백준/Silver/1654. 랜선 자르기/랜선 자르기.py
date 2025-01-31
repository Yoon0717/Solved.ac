import sys
input = lambda : sys.stdin.readline().rstrip()

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, sum(lan) // n

while start <= end:
    mid = (start+end) // 2
    line = 0
    for l in lan:
        line += l // mid
    if line >= n:
        start = mid + 1
    else:
        end = mid -1

print(end)