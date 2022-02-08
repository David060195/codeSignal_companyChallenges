def solution(t, allianceSize):
    maxEffort = 0
    if allianceSize <= 10:
        x = math.floor(t * 0.1)
        first = x * allianceSize
        second = 60 * allianceSize
        maxEffort = max(first, second)
    else:
        x = math.floor(t * 0.1)
        first = x * 10
        second = 60 * 10
        maxEffort = max(first, second)
    
    if t - maxEffort < 0:
        return 0
    return t - maxEffort