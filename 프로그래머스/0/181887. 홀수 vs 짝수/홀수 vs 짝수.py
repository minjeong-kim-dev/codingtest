def solution(num_list):
    answer1 = 0
    answer2 = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:              # i가 짝수
            answer1 += num_list[i]
        else:
            answer2 += num_list[i]
            
    if answer1 > answer2:
        return answer1
    
    return answer2