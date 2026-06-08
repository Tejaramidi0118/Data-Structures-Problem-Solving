class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        s = list(s)
        n = len(s)

        for i in range(0, n, 2*k):
            reverse(i, min(i+k- 1, n-1))

        return "".join(s)