def solution(my_string):
    answer = ''
    alpa = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i not in alpa:
            answer += i
    
    return answer