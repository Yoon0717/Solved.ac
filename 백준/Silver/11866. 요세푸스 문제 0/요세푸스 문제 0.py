import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
li = [i for i in range(1, n+1)]
yose = []

index = 0
k -= 1
while len(li) != 0:
    index = (index+k) % len(li)
    yose.append(str(li.pop(index)))

print('<'+', '.join(yose)+'>')