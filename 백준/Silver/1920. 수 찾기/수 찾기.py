import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input()) # A의 갯수
A = set(map(int, input().split()))
m = int(input()) # number 갯수
number = list(map(int, input().split()))

for num in number:
  print(1) if num in A else print(0)