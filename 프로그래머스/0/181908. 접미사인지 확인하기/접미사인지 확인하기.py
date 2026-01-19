def solution(my_string, is_suffix):
    answer = 0
    list = []
    
    for i in range(len(my_string)):
        list = my_string[i:]
        answer.append(list)
        
    if is_suffix in list:
        answer = 1
    else:
        answer = 0
    
    return answer