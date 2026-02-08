class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif not self.isMatching(stack[-1], char):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
    
    def isMatching(self, a: str, b: str) -> bool:
        return (a == '(' and b == ')') or \
               (a == '{' and b == '}') or \
               (a == '[' and b == ']')
