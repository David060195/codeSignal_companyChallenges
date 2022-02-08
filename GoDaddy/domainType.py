def solution(domains):
    m = {"info" : "information", "com" : "commercial", "net" : "network", "org" : "organization"}
    return [m[x.split(".")[-1]] for x in domains]