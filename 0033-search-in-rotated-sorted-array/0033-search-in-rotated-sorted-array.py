class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:  #Target Found
                return mid
            if nums[l]<=nums[mid]:  #check left is sorted
                if nums[l]<=target<nums[mid]:   #if sorted is target present 
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<=nums[r]:   #check r is sorted and is target present
                    l = mid+1
                else:
                    r = mid-1
        return -1  #-1 as targer was not found