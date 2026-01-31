def solution(strArr):
    data = {}
    max = 0
    
    for i in range(len(strArr)):
        
        if len(strArr[i]) not in data:
            data[len(strArr[i])] = 1
        else:
            data[len(strArr[i])] += 1
    
    for j in data:
        if data[j] > max:
            max = data[j]
    
    return max