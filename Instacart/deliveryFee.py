def deliveryFee(intervals, fees, deliveries):
    intervals.append(24)
    m = {}
    for i in range(len(intervals) - 1):
        m[tuple(range(intervals[i], intervals[i + 1]))] = 0
    for k, _ in m.items():
        for x, _ in deliveries:
            if x in k:
                m[k] += 1
    a = m.values()
    ans = []
    for x, y in zip(fees, a):
        if y == 0:
            return False
        ans.append(x / y)
    return all(x == ans[0] for x in ans)
