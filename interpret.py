class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if i > 0 and command[i] == ")" and command[i-1] == "(":
                result += "o"
            elif command[i] == "a":
                result += "a"
            elif command[i] == "l":
                result += "l"
            elif command[i] == "G":
                result += "G"
        return result