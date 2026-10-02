class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []

        def backtrack(curr,open,close):
            if len(curr) == 2*n:
                output.append("".join(curr))
                return
            
            if open < n:
                curr.append('(')
                backtrack(curr,open+1,close)
                curr.pop()
            
            if close < open:
                curr.append(')')
                backtrack(curr,open,close+1)
                curr.pop()
        
        backtrack([],0,0)

        return output