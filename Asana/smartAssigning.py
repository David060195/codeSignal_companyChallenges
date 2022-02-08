from collections import defaultdict
def solution(names, statuses, projects, tasks):
    n = len(names)
    m = defaultdict(list)
    for i in range(n):
        if not statuses[i]:
            m[names[i]].append(tasks[i])
            m[names[i]].append(projects[i])
    ans = sorted(m.items(), key=lambda x: x[1])
    
    return ans[0][0]