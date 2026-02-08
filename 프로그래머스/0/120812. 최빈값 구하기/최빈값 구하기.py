def solution(array):
    answer = 0
    data = {}
        
    for i in array:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1
    
    max_cnt = max(data.values())

    mode = [k for k, v in data.items() if v == max_cnt]
    
    if len(mode) > 1:
        return -1
            
    return mode[0]