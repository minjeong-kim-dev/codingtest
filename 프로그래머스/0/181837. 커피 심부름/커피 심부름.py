def solution(order):
    count = 0
    
    for menu in order:
        if "americano" in menu:
            count += 4500
        elif "cafelatte" in menu:
            count += 5000
        else:
            count += 4500
        
    return count