def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):     # numLog[1]부터 numLog의 길이만큼 반복
        diff = numLog[i] - numLog[i-1]  # ex) numLOg[1]과 numLog[2]의 차이
                   
        if diff == +1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == +10:
            answer += 'd'        
        elif diff == -10:
            answer += 'a'            
    
    return answer