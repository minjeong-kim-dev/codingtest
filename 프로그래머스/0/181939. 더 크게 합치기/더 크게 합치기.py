def solution(a, b):
    answer = 0
    
    answer1 = str(a)+str(b)
    answer2 = str(b)+str(a)
    
    if answer1 >  answer2:
        answer = int(answer1)
        
    else:
        answer = int(answer2)
    
    return answer