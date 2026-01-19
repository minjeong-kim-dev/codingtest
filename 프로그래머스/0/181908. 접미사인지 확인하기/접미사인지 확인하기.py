def solution(my_string, is_suffix):
    answer = 0
    lists = []
    
    for i in range(len(my_string)):
        suffix = my_string[i:]
        lists.append(suffix)
        
    if is_suffix in lists:
        answer = 1
    else:
        answer = 0
    
    return answer