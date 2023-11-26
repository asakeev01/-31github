import string

def checkIfPangram(self, sentence: str) -> bool:
    if len(sentence) < 26:
        return False
    alp = string.ascii_lowercase
    for i in alp:
        if i not in sentence:
            return False
    return True