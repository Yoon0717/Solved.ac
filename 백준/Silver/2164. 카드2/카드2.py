import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
if n == 1:
    print(1)
    exit()
deq = deque([i for i in range(2, n+1, 2)])

if n % 2 == 0:
    while len(deq) > 1:
        deq.popleft()
        num = deq.popleft()
        deq.append(num)
else:
    while len(deq) > 1:
        num = deq.popleft()
        deq.append(num)
        deq.popleft()

print(deq[0])