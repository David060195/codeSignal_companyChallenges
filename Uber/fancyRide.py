def solution(l, fares):
    cars = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    ans = 0
    for index in range(len(fares)):
        temp = fares[index] * l
        if temp > 20:
            ans = index
            break
    return cars[ans - 1]