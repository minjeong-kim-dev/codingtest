def solution(start_num, end_num):
    answer = []
    
    if start_num > end_num:
        for i in range(start_num, end_num-1, -1):
            answer.append(i)
    else:
        for i in range(start_num, end_num+1):
            answer.append(i)
    
    return answer