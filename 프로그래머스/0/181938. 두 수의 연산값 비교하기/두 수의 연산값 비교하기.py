def solution(a, b):
    answer = 0
    
    str_a = str(a)
    str_b = str(b)
    
    if int((str_a + str_b)) < (2 * a * b):
        answer =  2 * a * b
    
    elif int((str_a + str_b)) > (2 * a * b):
        answer =  str_a + str_b
        
    elif int((str_a + str_b)) == (2 * a * b):
        answer =  str_a + str_b
    
    return int(answer)