class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        keys = []
        for i in range(len(items1)):
            if items1[i][0] not in d:
                d[items1[i][0]] = items1[i][1]
                keys.append([items1[i][0]])
            else:
                d[items1[i][0]] += items1[i][1]
        for j in range(len(items2)):
            if items2[j][0] not in d:
                d[items2[j][0]] = items2[j][1]
                keys.append([items2[j][0]])
            else:
                d[items2[j][0]] += items2[j][1]
        keys.sort()
        for n in range(len(keys)):
            keys[n].append(d[keys[n][0]])
        return keys