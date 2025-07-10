class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask