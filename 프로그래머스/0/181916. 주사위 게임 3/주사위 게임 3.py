def solution(a, b, c, d):
    answer = 0
    
    arr = sorted([a,b,c,d])
    
    if arr[0] == arr [-1]:                              # 4개 모두 같을때
        answer = (1111 * arr[0])
        
    elif arr[0] == arr[2]:                              # 3개가 같을 때
        answer = (10 * arr[0] + arr[3]) ** 2
        
    elif arr[1] == arr[3]:                              # 3개가 같을 때
        answer = (10 * arr[1] + arr[0]) ** 2
        
    elif arr[0] == arr[1] and arr[2] == arr[3]:         # 2쌍이 같을 때
        answer = (arr[0] + arr[2]) * (abs(arr[0] - arr[2]))
        
    elif arr[0] == arr[1]:                              # 2개만 같고 나머지다 모두 다를 때
        answer = arr[2] * arr[3]            
                
    elif arr[1] == arr[2]:                              # 2개만 같고 나머지다 모두 다를 때
        answer = arr[0] * arr[3]      
        
    elif arr[2] == arr[3]:                              # 2개만 같고 나머지다 모두 다를 때
        answer = arr[0] * arr[1]      

    else:                                               # 모두 다를 때
        answer = min(arr)
    
    return answer