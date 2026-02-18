def solution(s):
    answer = ''
    
    for i in s:
        if s.count(i) < 2:
            answer += i
    
    answer = sorted(answer)
    
    return ''.join(answer)