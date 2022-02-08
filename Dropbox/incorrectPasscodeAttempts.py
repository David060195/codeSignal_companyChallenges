def solution(passcode, attempts):
    c = 0
    for x in attempts:
        if x != passcode:
            c += 1
        else:
            c = 0
        if c == 10:
            return True
    return False
            