def solution(s, d):
    size = len(s)
    c = 0
    m = 0
    idx = 0
    ans = []
    for i in range(size):
        if s[i] == d[i]: 
            c += 1
        else:
            c = 0
        if c > m:
            m = c
            idx = i
    ans.append(m)
    ans.append(idx - m + 1)
    if m == 0: 
        return [0, 0]
    else:
        return ans