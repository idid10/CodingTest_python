import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().split()))

def solution(N, K, arr):
    answer = 0
    start, end = 0, 0


    numberCount = defaultdict(int)

    while end < N:
        if numberCount[arr[end]] >= K:
            numberCount[arr[start]] -= 1
            start += 1
        else:
            numberCount[arr[end]] += 1
            end += 1
            answer = max(answer, end - start)

    return answer

result = solution(N, K, arr)
print(result)
