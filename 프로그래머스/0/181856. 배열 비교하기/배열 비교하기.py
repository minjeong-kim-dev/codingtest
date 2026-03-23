def solution(arr1, arr2):
    answer = 0
    total1 = 0
    total2 = 0
    
    if len(arr1) != len(arr2):
        if len(arr1) < len(arr2):
            answer = -1
        else:
            answer = 1
            
    else:
        total1 = sum(arr1)
        total2 = sum(arr2)
        
        if total1 > total2:
            answer = 1
        elif total1 < total2:
            answer = -1
        else:
            answer = 0
    
    return answer