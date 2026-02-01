def solution(rank, attendance):
    data = []
    
    for i in range(len(rank)):
        if attendance[i]:
            data.append((rank[i], i))   # rank의 (값, 인덱스 번호)
    
    data.sort()
    
    a = data[0][1]                      # 인덱스 번호
    b = data[1][1]
    c = data[2][1]
    
    return 10000 * a + 100 * b + c
