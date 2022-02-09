from statistics import stdev
def solution(orders, n):
    m = len(orders)
    start = m - n
    res = []
    for i in range(start, m):
        arr = orders[start : i + 1]
        values = []
        values.append(max(arr))
        values.append(sum(arr) / len(arr))
        values.append(-1)
        if len(arr) > 1:
            values[-1] = stdev(arr)
        res.append(values)
    return res
        