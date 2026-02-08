import math

def solution(numer1, denom1, numer2, denom2):

    new_denom = denom1 * denom2                         # 분자
    new_num = (numer1 * denom2) + (numer2 * denom1)     # 분모

    gcd = math.gcd(new_num, new_denom)
    
    return [new_num // gcd, new_denom // gcd]