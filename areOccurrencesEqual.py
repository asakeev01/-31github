def areOccurrencesEqual(self, s: str) -> bool:
    noRep = set(s)
    arr = []
    for i in noRep:
        arr.append(s.count(i))
    if len(set(arr)) != 1:
        return False
    else:
        return True