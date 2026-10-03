# class Solution:
#     def sortArray(self, nums: list[int]) -> list[int]:    #Bubble Sort
#         n = len(nums)
#         for i in range(n):
#             isSwap = False
#             for j in range(n-i-1):
#                 if nums[j]>nums[j+1]:
#                     #we will swap
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#                     isSwap = True

#             if not isSwap:
#                 break
#         return nums
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:   #Used GPT merge sort(Above is correct just not in topics so unable to submit)

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        ans = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        while i < len(left):
            ans.append(left[i])
            i += 1

        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans