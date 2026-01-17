def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        s = parts[i][0]
        e = parts[i][1]
        
        list = my_strings[i][s:e+1]     # my_strings의 i번째 인덱스를 가져와 [s:e+1]를 잘라서 list에 담기
        
        answer += list
            
    return answer