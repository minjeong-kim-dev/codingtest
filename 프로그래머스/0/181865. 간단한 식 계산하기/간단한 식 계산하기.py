def solution(binomial):
    answer = 0
    
    bin = binomial.split(' ')
    
    a = int(bin[0])
    op = bin[1]
    b = int(bin[2])
    
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    
    return answer