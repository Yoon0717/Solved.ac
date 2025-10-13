import sys
input = lambda : sys.stdin.readline().rstrip()

def queen(q):
  global ans
  if q == n: # n개의 queen을 완성했으면
    ans += 1
    return
  
  for i in range(n):
    if not columns[i] and not ups[q+i] and not downs[(n-1)+q-i] :
      columns[i] = True
      ups[q+i] = True
      downs[(n-1)+q-i] = True
      queen(q+1)
      columns[i] = False
      ups[q+i] = False
      downs[(n-1)+q-i]  = False

n = int(input())

columns = [False] * n
ups = [False] * (2*n-1) # 우상향 대각선
downs = [False] * (2*n-1) # 우하향 대각선
ans = 0
queen(0)

print(ans)