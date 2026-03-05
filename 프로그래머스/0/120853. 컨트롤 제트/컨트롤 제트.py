def solution(s):
    answer = 0
    data = []

    for i in s.split():
        if i != 'Z':
            data.append(int(i))
        else:
            data.pop()
            
    answer = sum(data)
    
    return answer