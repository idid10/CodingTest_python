import sys
input = sys.stdin.readline

end_num = []

n = int(input())
for i in range(10000000):
    if '666' in str(i):
        end_num.append(i)
print(end_num[n-1])
