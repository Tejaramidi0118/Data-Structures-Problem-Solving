class Solution:
    def strStr(self, haystack, needle):
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        # return haystack.index(needle[0]) if needle in haystack else -1