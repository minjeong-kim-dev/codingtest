def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        arr_ = arr[s:e+1]
        candidate = []
        
        for i in arr_:
            if i > k:       
                candidate.append(i)           
        if candidate:
            answer.append(min(candidate))

        else:  
            answer.append(-1)

    return answer