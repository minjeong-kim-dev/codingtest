def solution(a, b):
    answer = 0
    
    answer1 = int(str(a)+str(b))
    
    if answer1 > (2*a*b):
        answer = answer1
        
    else:
        answer = (2*a*b)
    
    return answer