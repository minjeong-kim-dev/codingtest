def solution(a, b):
    answer = 0
    
    str_a = str(a)
    str_b = str(b)
    
    if (str_a + str_b) > (str_b + str_a):
        answer = str_a + str_b
        
    elif (str_a + str_b) < (str_b + str_a):
        answer = str_b + str_a
    
    elif (str_a + str_b) == (str_b + str_a):
        answer = str_a + str_b
    
    return int(answer)