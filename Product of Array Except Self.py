# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/651ba72f606c1a7d9addbba5
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result =  [1] * n
         # Left products
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        # Right products
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
