import math
def solution(contractData):
    def median(s):
        l = len(s)
        if l % 2 == 1:
            return s[l // 2]
        else:
            return sum(s[l // 2 - 1 : l // 2 + 1]) / 2.0
    
    q = sorted(contractData)
    m = len(q)
    if len(q) < 2:
        return []
    a = median(q[: m // 2])
    b = median(q[m // 2 :])
    return [math.floor(a), int(b - 0.5) + 1]
        