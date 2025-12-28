def solution(arr, queries):
    
    for s, e, k in queries:         # queries의 0,4,1 / 0,3,2 / 0,3,3 을 반복
        for i in range(s, e+1):     # queries에서 0~4, 0~3, 0~3까지 반복
            if i % k == 0:          # k의 배수일때
                arr[i] += 1
    
    return arr