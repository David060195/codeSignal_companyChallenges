import datetime
from collections import defaultdict, Counter
from operator import itemgetter
def roadmap(tasks, queries):
    ans = [[] for _ in range(len(queries))]
    for index, (employee, date) in enumerate(queries):
        curDate = datetime.datetime.strptime(date, '%Y-%m-%d')
        for arr in tasks:
            title, startTask, endTask, employees = arr[0], datetime.datetime.strptime(arr[1], '%Y-%m-%d'), datetime.datetime.strptime(arr[2], '%Y-%m-%d'), arr[3:]
            if employee in employees and startTask <= curDate <= endTask:
                ans[index].append((endTask, title))
    for index, arr in enumerate(ans):
        ans[index] = sorted(arr, key = itemgetter(0, 1))
    for index, arr in enumerate(ans):
        ans[index] = [tittle for _, tittle in arr]
    return ans