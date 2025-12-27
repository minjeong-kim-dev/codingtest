def solution(arr):
    stk = []
    
    i = 0
    
    while i < len(arr):            # i가 arr의 길이보다 작을때 반복
        
        if len(stk) == 0:   
            stk.append(arr[i])
            i += 1
            
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
            
        elif stk[-1] >= arr[i]:
            stk.remove(stk[-1])
    
    return stk