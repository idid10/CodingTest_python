import sys
input = sys.stdin.readline

N = int(input())
A = list((map(int, input().split())))
min_v = A[0]
d = [0]*N

for i in range(1, N):
    min_v = min(min_v, A[i])
    d[i] = max(d[i-1], A[i]-min_v)

print(*d)