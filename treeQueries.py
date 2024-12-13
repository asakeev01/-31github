from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.maxLevel = {}
        allLevels = []
        s = deque()
        s.append(root)
        def dfs(node, level):
            if not node:
                return level
            else:
                left_level = dfs(node.left, level + 1)
                right_level = dfs(node.right, level + 1)
                max_subtree_level = max(left_level, right_level)
                self.maxLevel[node.val] = [level, max_subtree_level]
                return max_subtree_level
        dfs(root, 0)
        currLvl = self.maxLevel[root.val][0]
        temp = []
        while s:
            node = s.popleft()
            if currLvl != self.maxLevel[node.val][0]:
                temp.sort()
                allLevels.append(temp)
                temp = []
                currLvl = self.maxLevel[node.val][0]
            temp.append(self.maxLevel[node.val][1])
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        allLevels.append(temp)
        print(allLevels)
        print(self.maxLevel)
        ans = []
        for i in range(len(queries)):
            if allLevels[0][0] == self.maxLevel[queries[i]][1]:
                if len(allLevels[self.maxLevel[queries[i]][0]]) != 1:
                    ans.append(allLevels[self.maxLevel[queries[i]][0]][-2]-1)
                else:
                    ans.append(self.maxLevel[queries[i]][0]-1)
            else:
                ans.append(allLevels[0][0]-1)
        return ans