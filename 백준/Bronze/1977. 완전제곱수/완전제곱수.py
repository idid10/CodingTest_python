import sys
input = sys.stdin.readline

min_num = int(input())
max_num = int(input())
square = []

def issquare(num):
    temp = num ** 0.5
    if int(temp) == temp:
        if temp ** 2 == num:
            return True
    return False

for i in range(min_num, max_num+1):
    if issquare(i):
        square.append(i)
if square:
    print(sum(square), min(square))
else:
    print(-1)