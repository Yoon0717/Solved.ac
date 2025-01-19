import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    stack = []
    sen = input()

    if sen == '.':
        break

    is_bal = 'yes'
    for s in sen:
        if s == '(' or s == '[':
            stack.append(s)
        elif s ==')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s ==']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break
    
    if len(stack) != 0:
        print('no')
    else:
        print('yes')