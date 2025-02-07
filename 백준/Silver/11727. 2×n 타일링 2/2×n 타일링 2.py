import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input()) # 2xn 타일
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[-1] % 10007)