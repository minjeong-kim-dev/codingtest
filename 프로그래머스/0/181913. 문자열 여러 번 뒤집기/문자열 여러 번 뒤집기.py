def solution(my_string, queries):
    answer = ''
    arr = list(my_string)                    # my_string list로 변경
    
    for s,e in queries:                     
        arr[s : e+1] = arr[s : e+1][::-1]    # s부터 e까지 역순으로 만들기
    
    answer = ''.join(arr)                    # list를 문자열로 만들어주기
            
    
    return answer
