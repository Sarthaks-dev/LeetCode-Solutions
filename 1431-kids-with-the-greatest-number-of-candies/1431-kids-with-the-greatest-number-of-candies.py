class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxC = max(candies)
        ans = []
        for i in candies:
            if(i+extraCandies)>=maxC:
                ans.append(True)
            else:
                ans.append(False)
        return ans