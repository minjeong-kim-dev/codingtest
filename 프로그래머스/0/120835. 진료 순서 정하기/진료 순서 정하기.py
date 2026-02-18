def solution(emergency):
    answer = []
    sort_emergency = sorted(emergency, reverse=True)    # [76, 24, 3]
    
    for i in emergency:
        answer.append(sort_emergency.index(i) +1)
    
    return answer