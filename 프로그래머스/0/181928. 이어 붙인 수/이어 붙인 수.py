def solution(num_list):
    answer = ""
    even = ""
    odd = ""
    
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
            
    answer = int(even) + int(odd)
    
    return answer