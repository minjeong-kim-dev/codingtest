def solution(my_string):
    new_my_string = my_string.split()
    answer = int(new_my_string[0])
    
    for i in range(1, len(new_my_string), 2):
        op = new_my_string[i]
        nn = int(new_my_string[i+1])
        
        if op == '+':
            answer += nn
        else:
            answer -= nn
    
    return answer