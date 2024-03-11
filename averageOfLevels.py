class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        ans = []
        q.append(root)
        currLevel = 1
        currLevelCounter = 0
        nextLevel = 0
        counter = 0
        while q:
            node = q.popleft()
            counter += node.val
            currLevelCounter += 1
            if node.left:
                nextLevel += 1
                q.append(node.left)
            if node.right:
                nextLevel += 1
                q.append(node.right)
            if currLevelCounter == currLevel:
                counter = counter / currLevel
                ans.append(counter)
                counter = 0
                currLevel = nextLevel
                nextLevel = 0
                currLevelCounter = 0
        return ans