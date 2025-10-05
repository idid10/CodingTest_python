import sys
input = sys.stdin.readline

N = int(input())
grad = list(map(str, input().split()))
use = list(map(str, input().split()))

for item in use:
    grad.remove(item)

print(*grad)
