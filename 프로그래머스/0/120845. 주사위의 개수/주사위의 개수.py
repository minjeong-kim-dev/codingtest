def solution(box, n):
    answer = 0
    
    answer1 = box[0] // n
    answer2 = box[1] // n
    answer += (answer1*answer2) * (box[2] // n)
    
    return answer