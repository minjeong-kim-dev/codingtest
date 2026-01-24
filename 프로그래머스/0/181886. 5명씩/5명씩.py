def solution(names):
    answer = []
    result = []
    
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(i)
            
    for j in range(len(answer)):
        result.append(names[answer[j]])
            
    
    return result