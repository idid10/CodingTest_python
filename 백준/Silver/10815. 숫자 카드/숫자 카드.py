import sys
input = sys.stdin.readline

N = int(input())
mine = list(map(int, input().split()))
M = int(input())
q = list(map(int, input().split()))
tmp = {}
for i in range(len(mine)):
    tmp[mine[i]]=0

for j in range(M):
    if q[j] not in tmp:
        print(0, end= ' ')
    else:
        print(1, end = ' ')