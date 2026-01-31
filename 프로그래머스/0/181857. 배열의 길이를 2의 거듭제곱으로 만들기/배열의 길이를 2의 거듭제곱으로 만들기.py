def solution(arr):
    target = 1
    
    while target < len(arr):
        target *= 2
        
    while target > len(arr):
        arr.append(0)
    
    return arr