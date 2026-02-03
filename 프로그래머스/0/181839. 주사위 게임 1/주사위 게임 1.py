def solution(a, b):
    answer = 0
    
    if a % 2 == 1 and b % 2 == 1:       # 둘 다 홀수
        answer = a**2 + b**2
    
    elif  a % 2 == 1 or b % 2 == 1:     # 둘 중 하나가 홀수일때
        answer = 2 * (a + b)
    
    else:
        answer = abs(a - b)
    
    return answer