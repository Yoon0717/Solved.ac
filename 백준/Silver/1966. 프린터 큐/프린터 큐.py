import sys
input = lambda : sys.stdin.readline().rstrip()

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    out = 1
    while queue:
        if queue[0] < max(queue):
            queue.append(queue.pop(0))
        else:
            if m == 0:
                break
            queue.pop(0)
            out += 1
        m = m-1 if m > 0 else len(queue)-1

    print(out)
