class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        ans = 1
        s1 = set({})
        s1.add(s[0])
        i=0
        j=1
        while j<n:
            while s[j] in s1:
                s1.discard(s[i])
                i+=1
            s1.add(s[j])
            j+=1
            ans = max(ans,(j-i))
        return ans