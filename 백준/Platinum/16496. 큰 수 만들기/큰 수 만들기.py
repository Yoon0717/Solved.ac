import sys
from functools import cmp_to_key
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
number = list(input().split())

def compare(x, y):
    if x+y < y+x:
        return 1
    elif x+y == y+x:
        return 0
    else:
        return -1

number.sort(key=cmp_to_key(compare))

print(int("".join(number)))