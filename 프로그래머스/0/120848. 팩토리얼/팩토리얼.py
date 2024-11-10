def factorial(num):
    if num > 1 :
        return num * factorial(num-1)
    else:
        return 1

def solution(n):
    answer = 0
    while n >= factorial(answer):
        answer += 1
    return answer -1