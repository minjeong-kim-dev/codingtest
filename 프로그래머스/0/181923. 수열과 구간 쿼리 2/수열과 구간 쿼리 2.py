def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = []                       # 새로운 list 추가
        
        for i in range(s, e+1):
            if arr[i] > k:              # arr[i]가 k보다 클때 
                temp.append(arr[i])     # temp에 arr[i]추가
                            
        if not temp:                    # temp가 비어있을때
            answer.append(-1)
        else:                           # temp가 비어있지 않을때
            answer.append(min(temp))    # temp에서 제일 작은 값을 answer에 추가
    
    return answer