def solution(my_string, queries):
    answer = ''
    arr = list(my_string)
    
    for s,e in queries:
        arr[s : e+1] = arr[s : e+1][::-1]
        
    answer = ''.join(arr)        
    
    return answer