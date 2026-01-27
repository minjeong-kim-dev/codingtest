def solution(myString, pat):
    answer = 0
    str = ''
    
    for i in myString:
        if i == 'A':
            str += 'B'
        elif i == 'B':
            str += 'A'
            
    if pat in str:
        answer = 1
    else:
        answer = 0
            
    
    return answer