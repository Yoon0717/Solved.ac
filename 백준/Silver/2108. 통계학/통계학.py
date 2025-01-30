import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
li = []
dic = dict()

for _ in range(n):
    k = int(input())
    li.append(k)
    if k in dic:
        dic[k] += 1
    else:
        dic[k] = 1
li.sort()

num = max(dic.values())
mode = []

for k in dic:
    if num == dic[k]:
        mode.append(k)
mode.sort()

print(round(sum(li) / n))
print(li[n//2])
print(mode[0] if len(mode) == 1 else mode[1])
print(li[-1]-li[0])