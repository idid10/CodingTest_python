import sys
input= sys.stdin.readline

N, M = map(int, input().split())
note = {}
for i in range (N):
    add, pw = map(str, input().split())
    note[add] = pw

for i in range (M):
    q = input().rstrip()
    print(note[str(q)])