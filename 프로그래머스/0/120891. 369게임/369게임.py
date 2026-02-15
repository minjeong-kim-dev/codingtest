def solution(order):
    answer = 0
    a = '369'
    str_order = str(order)
    
    for i in str_order:
        if i in a:
            answer += 1
    
    return answer