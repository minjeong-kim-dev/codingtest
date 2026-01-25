def solution(my_string, alp):
    answer = ''
    
    for i in my_string:
        if alp in my_string:
            answer = my_string.replace(alp, alp.upper())
        else:
            answer = my_string

        
    return answer