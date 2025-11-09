import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pascal = [[] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0 or j == 0 or i == j:
            pascal[i].append(1)
        else:
            pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])

print(pascal[n-1][k-1])
