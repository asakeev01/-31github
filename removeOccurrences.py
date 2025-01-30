class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        is_part = True
        while is_part:
            is_part = False
            for i, letter in enumerate(s):
                if letter == part[0]:
                    s_ind = i
                    part_ind = 0
                    while s_ind < len(s) and part_ind < len(part) and s[s_ind] == part[part_ind]:
                        s_ind += 1
                        part_ind += 1
                    if part_ind == len(part):
                        is_part = True
                        s = s[:i] + s[s_ind:]
                        break
        return s