def solution(pros, distances, travelPreferences):
    a = []
    b = []
    for i in range(len(pros)):
        if travelPreferences[i] >= distances[i]:
            a.append((distances[i], pros[i]))
        else:
            b.append(((distances[i] - travelPreferences[i]), pros[i]))
    t = sorted(a) + sorted(b)
    ans = [x for _, x in t]
    return ans[0 : 5]