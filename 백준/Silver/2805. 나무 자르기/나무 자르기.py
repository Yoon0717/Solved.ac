import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split()) # n = 나무 수, m = 필요한 나무 길이
tree = list(map(int, input().split()))

high, low = max(tree), 0

while low <= high:
    mid = (low+high) // 2 # 절단기 높이 후보
    total = sum(t-mid for t in tree if t > mid)
    if total >= m:
        low = mid+1
    elif total < m:
        high = mid-1

print(high)