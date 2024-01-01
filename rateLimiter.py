class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.d:
            if timestamp >= self.d[message] + 10:
                self.d[message] = timestamp
                return True
            else:
                return False
        else:
            self.d[message] = timestamp
            return True