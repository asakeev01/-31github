class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def bt(used, temp):
            if len(temp) == len(pattern) + 1:
                return "".join(temp)

            for i in range(1, len(pattern) + 2):
                if i not in used:
                    if temp:
                        if pattern[len(temp) - 1] == "I" and temp[-1] > str(i):
                            continue
                        if pattern[len(temp) - 1] == "D" and temp[-1] < str(i):
                            continue

                    used.add(i)
                    temp.append(str(i))

                    result = bt(used, temp)
                    if result:
                        return result

                    temp.pop()
                    used.remove(i)

            return None

        return bt(set(), [])