import sys
input = lambda : sys.stdin.readline().rstrip()

pil = int(input())

bag = [1 for _ in range(1000)] + [1000 for _ in range(1000)]
print(len(bag))
print(*bag)