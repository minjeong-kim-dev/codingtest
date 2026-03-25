def solution(array):
    max_value = array[0]
    max_index = 0
    
    for i, num in enumerate(array):
        if num >= max_value:
            max_value = num
            max_index = i
        
    return [max_value, max_index]