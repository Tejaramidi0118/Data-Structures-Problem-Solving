class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = []

        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                n = 0
                while i < len(s) and s[i].isdigit():
                    n = n*10 + int(s[i])
                    i += 1
                num.append(n)
            elif s[i] == '[':
                stack.append(res)
                res = ""
                i += 1
            
            elif s[i] == ']':
                prev = stack.pop()
                n = num.pop()
                res = prev + n * res
                i += 1
            else:
                res += s[i]
                i += 1
  
        return res