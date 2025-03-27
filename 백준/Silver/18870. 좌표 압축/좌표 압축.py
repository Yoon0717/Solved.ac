import sys
input = lambda : sys.stdin.readline().rstrip()

# 리스트에서 자신보다 작은 값의 갯수 (값의 중복 X)
n = int(input())
coordinate = list(map(int, input().split()))
unique_sorted_coordinate = sorted(set(coordinate))

unique_sorted_dic = {v:i for i,v in enumerate(unique_sorted_coordinate)}

for i in coordinate:
    print(unique_sorted_dic[i], end=' ')