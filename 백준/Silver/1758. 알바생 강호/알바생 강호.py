import sys
input = sys.stdin.readline

n = int(input())

answer = 0


tip = [int(input()) for i in range(n)]
tip.sort(reverse=True)
#print(tip)

for i in range(n):
    if tip[i] - ((i+1)-1) > 0:
        answer += tip[i]-((i+1)-1)
    else:
        answer += 0

print(answer)
