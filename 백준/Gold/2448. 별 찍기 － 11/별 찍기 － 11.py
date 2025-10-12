import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stars = [[' ']*2*n for _ in range(n)] # 가로길이 = 2n, 세로길이 = n

def draw(x, y, size):
  if size == 3:
    stars[x][y] = '*'
    stars[x+1][y-1] = stars[x+1][y+1] = '*'
    for k in range(-2, 3):
      stars[x+2][y+k] = '*'
  else:
    draw(x, y, size//2)
    draw(x+size//2, y-size//2, size//2)
    draw(x+size//2, y+size//2, size//2)

draw(0, n-1, n)

for star in stars:
  print("".join(star))