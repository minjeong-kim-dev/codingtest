def solution(order):
    answer = 0
    a = ['3','6','9']
    
    for i in str(order):
        if i in a:
            answer += 1
    
    return answer