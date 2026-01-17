def solution(my_string):
    answer = []
    
    for i in range(len(my_string)): 
        list = my_string[i:]
        answer.append(list)
        answer.sort()
        
    return answer