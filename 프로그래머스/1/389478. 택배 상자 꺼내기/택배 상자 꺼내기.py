def stack_box(m, n, w):
    boxes = []
    num = 1
    for i in range(m): # 일단 순서대로 배열에 추가
        tmp = []
        for j in range(w):
            if num <= n:
                tmp.append(num)
            else:
                tmp.append(0)
            num += 1
        boxes.append(tmp)
        
    for i in range(m): # 짝수 층은 순서 반대로
        if i % 2 == 1:
            boxes[i].reverse()
            
    return boxes

def solution(n, w, num):
    if n % w == 0: 
        m = n // w # 만들어야하는 행 길이
    else:
        m = n // w + 1 

    boxes = stack_box(m, n, w)

    # num의 위치 찾기
    num_idx = -1
    
    for i in range(m):
        if num in boxes[i]:
            row = i
            col = boxes[i].index(num)
            break

    cnt = 0 
    
    for i in range(row, m): # 자기자신부터 세기
        if boxes[i][col] != 0:
            cnt += 1

    return cnt