def solution(l, r):
    answer = []

    for i in range(l, r+1):
        s = str(i)
        
        isTrue = True
        
        for c in s:
            if c not in ['0','5']:
                isTrue = False
                break
        if isTrue:
            answer.append(i)
            
    if not answer:
        answer.append(-1)
    
    return answer