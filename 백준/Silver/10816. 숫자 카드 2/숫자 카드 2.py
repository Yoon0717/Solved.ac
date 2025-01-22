import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

dic = {}
for k in n_list:
    if k in dic:
        dic[k] += 1
    else:
        dic[k] = 1

def binary(k, n_list, start, end):
    if end < start:
        return 0
    mid = (start+end)//2
    if k == n_list[mid]:
        return dic[k]
    elif k < n_list[mid]:
        return binary(k, n_list, start, mid-1)
    elif k > n_list[mid]:
        return binary(k, n_list, mid+1, end)

for k in m_list:
    count = binary(k, n_list, 0, len(n_list)-1)
    print(0 if count==None else count, end=' ')