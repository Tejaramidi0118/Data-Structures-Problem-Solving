class Solution:
    def getHappyString(self, n: int, k: int):
        
        def backtrack(curr, last):
            if len(curr) == n:
                ans.append(curr)
                return

            for ch in "abc":
                if ch == last:
                    continue

                backtrack(curr + ch, ch)

                if len(ans) >= k:
                    return
        
        ans = []
        backtrack("", "")
        
        if len(ans) < k:
            return ""
        
        return ans[k-1]