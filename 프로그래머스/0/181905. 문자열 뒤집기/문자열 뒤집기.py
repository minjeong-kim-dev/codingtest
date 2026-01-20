def solution(my_string, s, e):
    answer = ''
    result = list(my_string)
    result[s:e+1] = result[s:e+1][::-1]
    answer = ''.join(result)
        
    return answer