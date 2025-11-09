import sys
input = sys.stdin.readline

N = int(input())
route = str(input())
count = 0
for i in range(N):
    if 'EW' in route[i:i+2]:
        count += 1
        
    #print(route[i:i+2])

print(count)