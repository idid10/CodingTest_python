from itertools import combinations

import sys
input = sys.stdin.readline
tmp = []

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in combinations(nums, 3):
    if sum(i) <= M:
        tmp.append(sum(i))
print(max(tmp))