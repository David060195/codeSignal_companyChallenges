def solution(stocks, riskBudget):
    def getMaxSum(node, totalSum):
        sumMax = 0
        for i in xrange(node + 1, len(stocks)):
            if stocks[i][0] >= 0 and totalSum + stocks[i][1] <= riskBudget:
                sumMax = max(sumMax, getMaxSum(i, totalSum + stocks[i][1]))
        return sumMax + stocks[node][0]
    globalMax = 0
    for i in xrange(len(stocks)):
        if stocks[i][0] >= 0 and stocks[i][1] <= riskBudget:
            globalMax = max(globalMax, getMaxSum(i, stocks[i][1]))
    return globalMax