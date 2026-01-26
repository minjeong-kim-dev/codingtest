def solution(myString, pat):
    count = 0
    n = len(pat)
    
    for i in range(len(myString)):
        if pat == myString[i:i+n]:
            count += 1
    
    return count