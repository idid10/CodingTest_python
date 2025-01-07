import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
num.sort()
if n%2 == 0:
    print(num[n//2 -1])
else:
    print(num[n//2])