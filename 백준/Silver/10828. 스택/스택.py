import sys

stack = []    
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[len(stack)-1])
            del(stack[len(stack)-1])
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[len(stack)-1])