import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
now, stack, answer, possible = 1, [], [], True

for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        answer.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        possible = False

if possible:
    for a in answer:
        print(a)
else:
    print('NO')