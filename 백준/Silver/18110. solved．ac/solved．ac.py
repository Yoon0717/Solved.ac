import sys
input = lambda : sys.stdin.readline().rstrip()

def round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)


n = int(input())
if n == 0:
    print(0)
    exit()

trimmed = round(n*0.15)

li = []
for _ in range(n):
    li.append(int(input()))
li.sort()

hap = 0
for i in range(trimmed, n-trimmed):
    hap += li[i]

print(round(hap/(len(li)-2*trimmed)))