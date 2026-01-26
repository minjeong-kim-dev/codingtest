def solution(myString, pat):
    answer = ''
    n = len(pat)
    
    for i in range(len(myString)):
        if pat == myString[i:i+n]:
            answer = myString[0:i+n]
    
    return answer