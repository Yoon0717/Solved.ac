import sys
input = sys.stdin.readline

n, k = map(int, input().split())
country = []

for _ in range(n):
  country.append(list(map(int, input().split())))

country = sorted(country, key = lambda x : (-x[1], -x[2], -x[3]))

grade = 1 # 출력할 등수
add_grade = 1

if k == country[0][0]:
  print(grade)
else:
  for i in range(1, n):
    if country[i-1][1] == country[i][1] and country[i-1][2] == country[i][2] and country[i-1][3] == country[i][3]:
      add_grade += 1
    else:
      grade += add_grade
      add_grade = 1
    
    if k == country[i][0]:
      print(grade)
      break