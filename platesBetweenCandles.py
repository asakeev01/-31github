class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        platesBetCount = []
        lP = False
        rP = False
        counter = 0
        tempCounter = 0
        for i in range(len(s)):
            if s[i] == "|" and lP == True and rP == True:
                counter += tempCounter
                tempCounter = 0
            elif s[i] == "|" and lP == True:
                rP = True
                counter += tempCounter
                tempCounter = 0
            elif s[i] == "|":
                lP = True
                tempCounter = 0
            else:
                tempCounter += 1
            platesBetCount.append([counter])
        pointer = 0
        for k in range(len(s) - 1, -1, -1):
            if s[k] == "|":
                pointer = k
            else:
                platesBetCount[k].append(pointer)
        answer = []
        print(platesBetCount)
        for j in range(len(queries)):
            st = queries[j][0]
            fin = queries[j][1]
            if s[st] == "*":
                if platesBetCount[st][1] < fin:
                    st = platesBetCount[st][1]
                else:
                    answer.append(0)
                    continue
                if st == 0:
                    answer.append(0)
                    continue
            diff = platesBetCount[fin][0] - platesBetCount[st][0]
            answer.append(diff)
        return answer
