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
        for i in arr1:
            total1 += i
        for j in arr2:
            total2 += j
        
        if total1 > total2:
            answer = 1
        elif total1 == total2:
            answer = 0
        else:
            answer = -1
    
    return answer