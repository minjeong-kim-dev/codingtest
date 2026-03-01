def solution(array):
    answer = 0
    
    for i in array:
        i = str(i)
        
        if '7' in i:
            answer += i.count('7')
               
    return answer