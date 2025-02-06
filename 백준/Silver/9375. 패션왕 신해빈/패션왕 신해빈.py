import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    m = int(input())
    count = 1
    clothes = {}
    for _ in range(m):
        name, types = input().split()
        if types in clothes:
            clothes[types] += 1
        else:
            clothes[types] = 1
    for c in clothes:
        count *= clothes[c]+1
    print(count-1)