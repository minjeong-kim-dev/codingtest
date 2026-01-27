def solution(myString):
    answer = []
    
    myString_ = myString.split('x')
    
    for i in myString_:
        answer.append(len(i))
    
    return answer