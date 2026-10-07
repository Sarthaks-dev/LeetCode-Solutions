class Solution:
    def gethr(self,piles,mid):
        ans = 0
        for i in piles:
            ans+= (i+mid-1)//mid
        return ans
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        k = r
        while l<=r:
            mid = (l+r)//2
            if self.gethr(piles,mid)>h:
                l = mid+1
            else:
                k = mid
                r = mid-1
        return k
        