class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x:x[0])
        
        s = 0
        i = 0
        count = 0

        while s < time:
            far = s

            while i < len(clips) and clips[i][0] <= s:
                far = max(far,clips[i][1])
                i += 1
            
            if far == s:
                return -1
            
            count += 1
            s = far
        
        return count