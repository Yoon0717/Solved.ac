import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readlines()

preorder = list(map(int, input))

def postorder(order):
  if len(order) == 0:
    return
  
  left, right = [], []
  mid = order[0]
  
  for i in range(1, len(order)):
    if order[i] < mid:
      left.append(order[i])
    else:
      right.append(order[i])
  
  postorder(left)
  postorder(right)
  print(mid)

postorder(preorder)