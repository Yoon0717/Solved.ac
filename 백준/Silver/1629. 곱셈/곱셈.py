import sys
input = lambda : sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

def mul_mode(a, b, c):
  if b == 0:
    return 1
  half = mul_mode(a, b//2, c)
  half_mod = (half * half) % c
  if b % 2 == 0:
    return half_mod
  else:
    return ((half_mod * a) % c ) % c

print(mul_mode(a%c, b, c))