def solution(polynomial):
    answer = ''
    constant = 0
    coe = 0
    tmp = polynomial.split(' ')
    num = []
    
    for i in tmp:
        if 'x' in i:
            num.append(i)
        elif i != "+":
            constant += int(i)
            
    for i in num:
        if i == 'x':
            coe += 1
        else:
            coe += int(i[:-1])
    if constant == 0 and coe != 0:
        if coe == 1:
            answer = 'x'
        else:
            answer = str(coe) + 'x'
    elif coe == 0 and constant != 0:
        answer = str(constant)
    elif constant == 0 and coe == 0:
        answer = '0'
    else:
        if coe == 1:
            answer = 'x' + ' + ' + str(constant)
        else:
            answer = str(coe) + 'x' + ' + ' + str(constant)
    
    return answer