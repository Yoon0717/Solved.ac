import sys
from math import sqrt
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if sqrt(i) == int(sqrt(i)):
        dp[i] = 1
    else:
        j = 1
        while j <= sqrt(i):
            if dp[i] == 0:
                dp[i] = dp[j**2] + dp[i - j**2]
            else:
                dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])
            j += 1

print(dp[n])