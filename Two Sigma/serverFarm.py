def solution(jobs, servers):
    a = []
    s = [[] for _ in range(servers)]
    for index, value in enumerate(jobs):
        a.append((value, index))
    a = sorted(a, key = lambda x: (x[0], -x[1]), reverse = True)
    status = [0 for _ in range(servers)]
    for i in range(servers):
        if a:
            t = a.pop(0)
            s[i].append(t[1])
            status[i] = t[0]
    while a:
        t = a.pop(0)
        m = status.index(min(status))
        s[m].append(t[1])
        status[m] += t[0]
    return s