def solution(my_string, is_prefix):
    answer = 0
    list = []
    
    for i in range(len(my_string)):
        prefix = my_string[:i]
        list.append(prefix)
        
        if is_prefix in list:
            answer = 1
        else:
            answer = 0
    
    return answer