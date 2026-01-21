import string

def solution(my_string):
    answer = [0] * 52
    
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    
    for i in my_string:
        idx = alphabet.index(i)
        answer[idx] += 1 
        
    
    return answer