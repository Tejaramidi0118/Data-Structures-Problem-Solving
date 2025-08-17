class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int length = 0;
        int[] freq = new int[128];
        int n = s.length();

        for(int right=0;right<n;right++){
            char currentChar = s.charAt(right);
            freq[currentChar]++;

            while(freq[currentChar] > 1){
                freq[s.charAt(l)]--;
                l++;
            }

            length = Math.max(length,right-l+1);
        }
        return length;

    }
}