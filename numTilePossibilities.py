class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def bt(tiles, visited, temp, answer):
            for i in range(len(tiles)):
                if i not in visited:
                    visited.add(i)
                    temp += tiles[i]
                    if temp not in answer:
                        answer.add(temp)
                    bt(tiles, visited, temp, answer)
                    visited.remove(i)
                    temp = temp[:-1]
        answer = set()
        bt(tiles, set(), "", answer)
        return len(answer)