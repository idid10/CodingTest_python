import sys
input= sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    case = list(input().split())
    print("Case #" + str(i) + ":", end= ' ')
    while case:
        print(case.pop(), end = ' ')
