def solution(n, t, edges):
    graph = { node : set() for node in range(n) }
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    def getExpectedTime(node, seen):
        seen.add(node)
        connectedNodeSum = sum(t[e] for e in graph[node] - seen)
        numberConnected = len(graph[node] - seen) or 1
        totalExpectTime = 0
        for n in graph[node] - seen:
           totalExpectTime += getExpectedTime(n, seen) 
        return t[node] + (totalExpectTime / numberConnected)
    minReadTime, res = float('inf'), 0
    for node in range(n):
        seen = set()
        expectedTime = getExpectedTime(node, seen)
        if expectedTime < minReadTime:
            minReadTime = expectedTime
            res = node
    return res
