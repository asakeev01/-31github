def reverseWords(self, s: str) -> str:
    words = s.split(" ")
    for i in range(len(words)):
        word = ""
        last = len(words[i]) - 1
        for k in range(last, -1, -1):
            word = word + words[i][k]
        words[i] = word
    ans = ""
    for j in range(len(words)):
        if j == len(words) - 1:
            ans += words[j]
        else:
            ans = ans + words[j] + " "
    return ans