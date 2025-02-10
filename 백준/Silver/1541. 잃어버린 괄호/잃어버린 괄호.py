import sys
input = lambda : sys.stdin.readline().rstrip()

latex = input().split('-')
new_latex = []

for l in latex:
  if '+' in l:
    sub_latex = map(int, l.split('+'))
    sub_sum = sum(sub_latex)
    new_latex.append(sub_sum)
  else:
    new_latex.append(int(l))

s = 0
for i in range(len(new_latex)):
  if i == 0:
    s += new_latex[i]
  else:
    s -= new_latex[i]

print(s)