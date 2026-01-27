def solution(myStr):
    answer = []

    for i in ['a', 'b', 'c']:
        myStr = myStr.replace(i, ' ')
        
    answer = myStr.split()
    
    return answer if answer else ["EMPTY"]

