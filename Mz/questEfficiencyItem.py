def solution(h, points, timeForQuests):
    def getMaxPoints(index, sumHour):
        maxPoint = points[index]
        for i in range(index + 1, len(h)):
            if sumHour + h[i] <= timeForQuests:
                maxPoint =  max(maxPoint, getMaxPoints(i, sumHour + h[i]) + points[index])
        return maxPoint
    maxGlobal = 0
    for index in range(len(h)):
       if h[index] <= timeForQuests:
           maxGlobal =  max(maxGlobal, getMaxPoints(index, h[index]))
    return maxGlobal
