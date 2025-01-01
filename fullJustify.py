class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        currChars = maxWidth
        currLine = ""
        i = 0
        line = []
        while i < len(words):
            if currChars == maxWidth:
                currChars -= len(words[i])
                line.append(words[i])
                i += 1
            elif len(words[i]) < currChars:
                currChars = currChars - (len(words[i]) + 1)
                line.append(words[i])
                i += 1
            else:
                spaces = 0
                extraSpaces = 0
                if len(line)-1 != 0:
                    spaces = currChars // (len(line)-1)
                    extraSpaces = currChars % (len(line)-1)
                else:
                    spaces = 0
                    extraSpaces = currChars
                for k in range(len(line)):
                    if k == len(line) - 1:
                        currLine = currLine + line[k] + " "*extraSpaces
                    else:
                        currLine = currLine + line[k] + " "
                        if spaces:
                            currLine = currLine + " "*spaces
                        if extraSpaces:
                            currLine = currLine + " "
                            extraSpaces -= 1
                lines.append(currLine)
                currLine = ""
                currChars = maxWidth
                line = []
        if line:
            for k in range(len(line)):
                if k == len(line) - 1:
                    currLine = currLine + line[k] + " " * currChars
                else:
                    currLine = currLine + line[k] + " "
            lines.append(currLine)
        return lines
