def solution(n):
    answer = []
    s = 2
    
    while s <= n:
        if n % s == 0:
            if s not in answer:
                answer.append(s)
            n = n //s
            
        else:
            s += 1
            
    return answer