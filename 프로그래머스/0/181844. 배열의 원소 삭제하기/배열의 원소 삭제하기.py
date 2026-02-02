def solution(arr, delete_list):
    answer = []
    
    for q in arr:
        if q not in delete_list:
            answer.append(q)
    
    return answer