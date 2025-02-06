import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = list(map(int, input().split()))
sum_array = [0]

total = 0
for a in array:
    total += a
    sum_array.append(total)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_array[j]-sum_array[i-1])