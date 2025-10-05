import sys
input = sys.stdin.readline

std = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28, 29, 30]

num = []

for i in range(28):
    std.remove(int(input()))

print(sorted(std)[0])
print(sorted(std)[-1])
