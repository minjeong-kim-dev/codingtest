def solution(numbers):
    answer = 0
    sum_num = 0
    n = len(numbers)
    
    for i in numbers:
        sum_num += i
    
    answer = sum_num / n
    
    return answer