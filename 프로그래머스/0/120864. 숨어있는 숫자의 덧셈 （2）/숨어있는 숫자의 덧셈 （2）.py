def solution(my_string):
    answer = 0
    for i in my_string:
        while i.isdigit():
            answer += int(i)
    return answer