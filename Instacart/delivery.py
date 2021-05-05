def delivery(order, shoppers):
    ans = []
    for x, y, z in shoppers:
        time = ((x + order[0]) / y) + z
        if time >= order[1] and time <= order[1] + order[2]:
            ans.append(True)
        else:
            ans.append(False)
    return ans