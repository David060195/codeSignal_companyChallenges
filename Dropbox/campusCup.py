from collections import defaultdict
from operator import itemgetter
def solution(emails):
    freq = defaultdict(int)
    for s in emails:
        _, domain = s.split("@")
        freq[domain] += 20
    for k, v in freq.items():
        if v < 100:
            v = 0
        elif v >= 100 and v < 200:
            v = -3
        elif v >= 200 and v < 300:
            v = -5
        elif v >= 300 and v < 500:
            v = -15
        else:
            v = -25
        freq[k] = v
    return [e[0] for e in sorted(freq.items(), key = itemgetter(1, 0))]