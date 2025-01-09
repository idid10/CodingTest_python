import sys
input = sys.stdin.readline
N, C = map(int,input().split())
weights = list(map(int,input().split()))
weights.sort()

def binary_search(left,right,diff):
    while left <= right:
        mid = (left + right)//2
        if weights[mid] == diff:
            return 1
        elif weights[mid] > diff:
            right = mid - 1
        else:
            left = mid + 1
    return 0

def check(N, C):
    if C in weights:
        return 1
    i, j = 0, N-1
    while i < j:
        total = weights[i] + weights[j]
        if total > C:
            j -= 1
        elif total == C:
            return True
        else:
            diff = C - total
            if weights[i] != diff and weights[j] != diff and binary_search(i,j,diff):
                return True
            i += 1
          
if check(N, C):
    print(1)
else:
    print(0)