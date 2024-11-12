def solution(n):
    answer = 0
    num = []
    for i in range(4, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                num.append(j)
        if len(num) >= 3:
            answer += 1
            num = []
        num = []
    return answer