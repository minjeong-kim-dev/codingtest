def solution(num_list):
    answer = 0
    summ = 0
    mul = 1
    
    for i in num_list:
        mul *= i
        summ += i
        
    if mul < (summ ** 2):
        answer = 1
    else:
        answer = 0
        
    return answer