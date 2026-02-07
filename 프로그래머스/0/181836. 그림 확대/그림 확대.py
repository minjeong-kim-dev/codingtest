def solution(picture, k):
    answer = []
    
    for i in picture:
        data = ''
        
        for j in i:
            data += j * k
            
        for _ in range(k):
            answer.append(data)
    
    return answer