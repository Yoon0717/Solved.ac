import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
# print(paper)

def is_same(paper, k, x, y):
    color = paper[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if paper[i][j] != color:
                return False
    return True

def devide_conquer(paper, k, x, y):
    if is_same(paper, k, x, y):
        if paper[x][y] == 0:
            return 1, 0
        else:
            return 0, 1
    
    half_k = k // 2
    white, blue = 0, 0
    for i in range(2):
        for j in range(2):
            new_x, new_y = x+i*half_k, y+j*half_k
            new_white, new_blue = devide_conquer(paper, half_k, new_x, new_y)
            white += new_white
            blue += new_blue
    return white, blue

white, blue = devide_conquer(paper, n, 0, 0)
print(white)
print(blue)