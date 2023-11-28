def countDigits(self, num: int) -> int:
    counter = 0
    for i in str(num):
        if num % int(i) == 0:
            counter += 1
    return counter