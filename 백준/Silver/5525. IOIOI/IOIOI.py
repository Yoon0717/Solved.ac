import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input()) # Pn의 n
m = int(input()) # sen의 길이
sen = input()

length = 0 # IOI의 갯수
count = 0 # Pn의 갯수

i = 1
while i < (m-1):
    if sen[i-1] == 'I' and sen[i] == 'O' and sen[i+1] == 'I':
        length += 1
        i += 2
    else:
        if length-n+1 > 0:
            count += (length-n+1)
        i += 1
        length = 0

if length-n+1 > 0:
     count += (length-n+1)
     
print(count)