def solution(numbers):
    numbers.sort()
    
    max_num1 = numbers[-1] * numbers[-2]       
    max_num2 = numbers[0] * numbers[1]
    
    return max(max_num1, max_num2)