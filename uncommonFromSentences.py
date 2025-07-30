from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        count = Counter(words)
        return [word for word, freq in count.items() if freq == 1]