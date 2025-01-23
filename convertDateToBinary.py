class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = date.split("-")
        new = []
        for el in lst:
            new.append(bin(int(el))[2:])

        st = '-'.join(new)
        return st