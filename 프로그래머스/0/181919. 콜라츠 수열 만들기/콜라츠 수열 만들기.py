def solution(n):
    answer = [n]            # n을 넣어줌(연산후 추가시에는 주어진 n값을 넣을 수 없음 => n은 변함)
            
    while n != 1:           # n이 1이 아닐때까지 반복
        if n % 2 == 0:      # 짝수일때
            n = n // 2      # 몫의 값을 n으로 함

        elif n % 2 != 0:    # 홀수일때
            n = 3 * n + 1   
            
        answer.append(n)    # 리스트에 추가해주기
    
    return answer