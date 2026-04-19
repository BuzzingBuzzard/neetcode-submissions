class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            print(stack)
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if bracket_map[curr] != char:
                    return False
        if len(stack) != 0:
            return False
        return True