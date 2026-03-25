def solution(myString, pat):
    answer = 0
    n = len(pat)
    
    for i in range(len(myString)):
        if pat in myString[i:i+n]:
            answer += 1
        
    
    return answer