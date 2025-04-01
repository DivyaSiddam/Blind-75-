# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/651bf54216a05eb7a5823779
class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_product = min_product = result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)
            
            result = max(result, max_product)
        
        return result
