def solution(img):
    def check(x, y):
        return x >= 0 and x < len(img) and y >= 0 and y < len(img[0])
    ans = [[0 for i in range(len(img[0]))] for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[i])):
            s = 0
            c = 0
            for a, b in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                x1 = i + a
                y1 = j + b
                if check(x1, y1):
                    s += img[x1][y1]
                    c += 1
            ans[i][j] = s / c
    return ans