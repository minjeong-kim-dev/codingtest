def solution(n):
    answer = 0
    
    if int(n**0.5)**2 == n:    # n의 제곱근을 구하고 정수로 바꾼 뒤 다시 제곱하여 원래 수와 비교
        answer = 1
    else:
        answer = 2
    
    return answer