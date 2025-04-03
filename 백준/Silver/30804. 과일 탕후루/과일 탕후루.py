import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
fruit = list(map(int, input().split()))
fruit_dic = {} # 각 과일의 갯수
count = 0 # 과일 갯수
l = 0
ans = 0 # 과일 길이는 현재 r-l로 알 수 있음 (굳이 len(fruit_list) 할 필요 X)

for r in range(n):
  if fruit[r] in fruit_dic:
    fruit_dic[fruit[r]] += 1
  else:
    fruit_dic[fruit[r]] = 1
    count += 1
    
    while count > 2:
      fruit_dic[fruit[l]] -= 1
      if fruit_dic[fruit[l]] == 0:
        del fruit_dic[fruit[l]]
        count -= 1
      l += 1
      
  ans = max(ans, r-l+1)

print(ans)