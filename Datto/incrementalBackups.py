def solution(lastBackupTime, changes):
    ans = []
    for x, y in changes:
        if x > lastBackupTime:
            ans.append(y)
    return sorted(list(set(ans)))
