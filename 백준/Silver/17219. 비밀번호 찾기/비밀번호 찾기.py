import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

site = {}
for _ in range(n):
    url, password = input().split()
    site[url] = password

for _ in range(m):
    print(site[input()])