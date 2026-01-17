def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:           # intStrs의 요소를 반복("0123456789","9876543210","9999999999999")
        list = i[s : s+l]       # s부터 s+l까지의 길이에 해당하는 것을 뽑아 list에 담기
            
        num = int(list)         # 문자열 list를 int로 바꿔주기
        
        if num > k:             
            answer.append(num)  # num이 k보다 클 때만 answer에 추가
        
    
    return answer