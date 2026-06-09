def solution(str1, str2):
    answer = ''
    lenn = len(str1)
    
    for i in range(lenn):
        answer += (str1[i] + str2[i])
    
    return answer