class Solution:
    def isValid(self, s: str) -> bool:
        matching_hash = {
            "}" : "{",
            ")" : "(",
            "]" :"[",
        }

        stack = []

        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)

            elif stack and stack[-1] != matching_hash[char]:
                return False

            elif stack and stack[-1] == matching_hash[char]:
                stack.pop(-1)
            else:
                return False
        if len(stack) < 1:
            return True
        else:
            return False