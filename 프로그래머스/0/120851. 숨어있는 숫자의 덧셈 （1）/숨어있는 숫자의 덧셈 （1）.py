def solution(my_string):
    answer = 0
    
    for i in my_string:
        if i.isdigit():         # i가 숫자인지 확인
            answer += int(i)
    
    return answer