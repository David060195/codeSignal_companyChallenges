from collections import defaultdict
def solution(topicIds, answerIds, views):
    topicsIndex = defaultdict(list)
    for index, topic in enumerate(topicIds):
        for topicId in topic:
            topicsIndex[topicId].append(index)
    answerToViews = {}
    for view in views:
        answerToViews[view[0]] = view
    def getViewByAnswerId(topicId):
        totalAnswers = []
        countViewsById = defaultdict(int)
        for index in topicsIndex[topicId]:
            for answer in answerIds[index]:
                totalAnswers.append(answer)
        for answer in totalAnswers:
            viewArr = answerToViews[answer]
            countViewsById[viewArr[1]] += viewArr[2]
        res = []
        for key, value in countViewsById.items():
            res.append([key, value])
        res.sort(key = lambda x : (x[1], -x[0]), reverse = True)
        return res
    res = []
    for topic in sorted(topicsIndex.keys()):
        res.append(getViewByAnswerId(topic))
    return res
