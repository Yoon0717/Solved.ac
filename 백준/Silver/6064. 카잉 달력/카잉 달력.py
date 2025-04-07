import sys
from math import lcm
input = lambda : sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    max_year = lcm(M, N) # 최소공배수
    ans = -1

    for k in range(max_year // M):
        year = M * k + x
        
        if (year-1) % N + 1 == y:
            ans = year
            break
    
    print(ans)