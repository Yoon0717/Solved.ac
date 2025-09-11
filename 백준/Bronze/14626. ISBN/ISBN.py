import sys
input = lambda : sys.stdin.readline().rstrip()

isbn = input()

check_num = int(isbn[-1])
answer = 10 - check_num if check_num != 0 else 0
total = 0
triple = False

for i in range(12):
  if i % 2 == 0:
    if isbn[i] =='*':
      continue
    total += int(isbn[i])
  else:
    if isbn[i] =='*':
      triple = True
      continue
    total += 3*int(isbn[i])

if triple:
  for n in range(0, 10):
    if (total + 3*n) % 10 == answer:
      print(n)
      break
else:
  for n in range(0, 10):
    if (total + n) % 10 == answer:
      print(n)
      break