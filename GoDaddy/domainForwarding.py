from collections import defaultdict
def solution(redirects):
    graph = defaultdict(set)
    uniqueRedirect = set()
    for u, v in redirects:
        uniqueRedirect.add(u)
        uniqueRedirect.add(v)
    countRedirect = { redirect : 0 for redirect in uniqueRedirect }
    for u, _ in redirects:
        countRedirect[u] += 1
    for u, v in redirects:
        graph[u].add(v)
        graph[v].add(u)
    seenGraph = set()
    def getRedirectGroup(redirect, group):
        group.append(redirect)
        seenGraph.add(redirect)
        for e in graph[redirect] - seenGraph:
            getRedirectGroup(e, group)
    groupByLastDomain = {}
    for k, v in countRedirect.items():
        if v == 0:
            group = []
            getRedirectGroup(k, group)
            groupByLastDomain[k] = sorted(group)
    res = []
    for k in sorted(groupByLastDomain.keys()):
        res.append(groupByLastDomain[k])
    return res