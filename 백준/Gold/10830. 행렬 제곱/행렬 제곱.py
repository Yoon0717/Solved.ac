import sys
input = lambda : sys.stdin.readline().rstrip()

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul(m1, m2):
  matrix = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        matrix[i][j] += m1[i][k] * m2[k][j] % 1000
  return matrix

def square(matrix, n):
  if n == 1:
    return matrix
  
  half = square(matrix, n//2)
  if n % 2 == 0:
    return mul(half, half)
  else:
    return mul(mul(half, half), matrix)

ans = square(A, B)

for i in range(N):
  for j in range(N):
    ans[i][j] %= 1000

for a in ans:
  print(*a)