import sys
input = sys.stdin.readline

n = int(input())
five = n//5 #5원 개수
two = 0 #2원 개수
current = 0

while True:
    current = n - (five*5) - (two*2)

    if five < 0 :
        print(-1)
        break
    
    if current == 0:
        print(five + two)
        break
        
    if current %2 != 0:
        five -= 1
    else :
        two = current//2