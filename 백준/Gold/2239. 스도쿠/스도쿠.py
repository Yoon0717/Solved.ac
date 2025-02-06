import sys
input = lambda : sys.stdin.readline().rstrip()

# 1. 시작점을 [0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]
# 2. 0의 좌표를 리스트에 저장

sudoku = [list(map(int, list(input()))) for _ in range(9)]
blank = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def available(y, x, num):
    # 가로 및 세로 확인
    for i in range(9): # 가로 세로 확인
        if sudoku[y][i] == num or sudoku[i][x] == num:
            return False
    # 3x3 박스 확인
    for i in range(3):
        for j in range(3):
            if sudoku[y//3*3+i][x//3*3+j] == num:
                return False
    # 겹치는거 없음
    return True

def dfs(n):
    if n == len(blank):
        for s in sudoku:
            print(*s, sep='')
        exit()
    
    y,x = blank[n]
    for num in range(1, 10):
        if available(y, x, num):
            sudoku[y][x] = num
            dfs(n+1)
            sudoku[y][x] = 0

# print()
dfs(0)