class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        prevState = 1
        self.currTime = arrival[0]
        self.finalTime = arrival[-1]
        self.personId = 0
        self.personIds = len(arrival)
        ans = [0]* self.personIds
        enteringList = []
        exitingList = []
        while self.personId < self.personIds or enteringList or exitingList:
            while self.personId < self.personIds and arrival[self.personId] <= self.currTime:
                if state[self.personId] == 1:
                    exitingList.append(self.personId)
                else:
                    enteringList.append(self.personId)
                self.personId += 1
            if prevState:
                if exitingList:
                    ans[exitingList.pop(0)] = self.currTime
                elif enteringList:
                    ans[enteringList.pop(0)] = self.currTime
                    prevState = 0
            else:
                if enteringList:
                    ans[enteringList.pop(0)] = self.currTime
                elif exitingList:
                    ans[exitingList.pop(0)] = self.currTime
                    prevState = 1
                else:
                    prevState = 1
            self.currTime += 1
        return ans