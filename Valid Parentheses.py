# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/651b9a965484cc24b7a16a26
class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack
